"""Read local text/Markdown/HTML/DOCX into source-labeled text. No converters installed."""
import argparse,hashlib,json,zipfile
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

class Visible(HTMLParser):
    def __init__(self):super().__init__(convert_charrefs=True);self.skip=0;self.parts=[]
    def handle_starttag(self,tag,attrs):
        if tag in ('script','style'):self.skip+=1
        elif tag in ('p','div','br','li','h1','h2','h3','tr'):self.parts.append('\n')
    def handle_endtag(self,tag):
        if tag in ('script','style') and self.skip:self.skip-=1
    def handle_data(self,data):
        if not self.skip:self.parts.append(data)

def extract(path):
    p=Path(path);data=p.read_bytes();suffix=p.suffix.lower();loss=[]
    if len(data)>50_000_000:raise ValueError('input exceeds 50 MB limit')
    if suffix in ('.md','.txt'):text=data.decode('utf-8-sig')
    elif suffix in ('.html','.htm'):
        parser=Visible();parser.feed(data.decode('utf-8-sig'));text=''.join(parser.parts);loss=['Layout, images, CSS visibility and dynamic content not represented']
    elif suffix=='.docx':
        with zipfile.ZipFile(p) as z:
            info=z.getinfo('word/document.xml')
            if info.file_size>20_000_000:raise ValueError('DOCX XML exceeds 20 MB limit')
            doc=ET.fromstring(z.read(info))
        ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        text='\n'.join(''.join(t.text or '' for t in para.findall('.//w:t',ns)) for para in doc.findall('.//w:p',ns))
        loss=['Only main-document paragraph text; images, layout, notes, revisions and embedded objects need separate inspection']
    else:raise ValueError('supported: UTF-8 TXT/MD/HTML and DOCX; PDF/EPUB require an available dedicated extractor')
    return {'source':str(p.resolve()),'sha256':hashlib.sha256(data).hexdigest(),'format':suffix,'losses':loss,
            'lines':[{'line':i+1,'text':t} for i,t in enumerate(text.splitlines())],
            'source_content_is_data':True}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');a=p.parse_args()
    try:print(json.dumps(extract(a.input),ensure_ascii=False))
    except (OSError,ValueError,KeyError,zipfile.BadZipFile,ET.ParseError) as e:p.exit(2,str(e)+'\n')
