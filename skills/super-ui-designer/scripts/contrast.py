"""Opaque sRGB contrast pairs. No inference about rendered styles or conformance."""
import itertools, json, re, sys

def luminance(value):
    if not isinstance(value,str) or not re.fullmatch(r'#?[0-9a-fA-F]{6}',value):
        raise ValueError('colors must be opaque six-digit sRGB hex')
    value=value.lstrip('#');channels=[int(value[i:i+2],16)/255 for i in (0,2,4)]
    linear=[c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4 for c in channels]
    return sum(a*b for a,b in zip(linear,(0.2126,0.7152,0.0722)))

def ratio(a,b):
    high,low=sorted((luminance(a),luminance(b)),reverse=True)
    return (high+0.05)/(low+0.05)

def analyze(data):
    colors=data['colors'];pairs=data.get('pairs')
    if not isinstance(colors,dict) or len(colors)<2: raise ValueError('at least two named colors required')
    for value in colors.values(): luminance(value)
    if pairs is None:
        rows=[{'fg':a,'bg':b,'ratio':ratio(colors[a],colors[b])} for a,b in itertools.combinations(colors,2)]
        return {'mode':'matrix','conformance':'UNVERIFIED','pairs':rows}
    if not isinstance(pairs,list) or not pairs: raise ValueError('pairs must be a nonempty list')
    rows=[]
    for pair in pairs:
        if pair.get('use') not in ('text','large_text','ui'):raise ValueError('use must be text, large_text, or ui')
        for role in ('fg','bg'):
            if pair.get(role) not in colors:raise ValueError(f'{role} must name a color in colors; available: {", ".join(map(str,colors))}')
        floor={'text':4.5,'large_text':3.0,'ui':3.0}[pair['use']]
        value=ratio(colors[pair['fg']],colors[pair['bg']])
        rows.append(dict(pair,ratio=value,floor=floor,status='PASS' if value>=floor else 'FAIL'))
    return {'mode':'specified pairs','status':'PASS' if all(r['status']=='PASS' for r in rows) else 'FAIL','pairs':rows,'whole_page_conformance':'UNVERIFIED'}

if __name__=='__main__':
    try:
        with open(sys.argv[1],encoding='utf-8-sig') as f:result=analyze(json.load(f))
        print(json.dumps(result));sys.exit(result.get('status')=='FAIL')
    except (OSError,ValueError,KeyError,TypeError,IndexError) as e:print(json.dumps({'error':str(e)}));sys.exit(2)
