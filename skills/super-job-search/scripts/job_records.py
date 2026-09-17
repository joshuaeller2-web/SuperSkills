"""Normalize job identities and audit explicit candidate claims; never submit forms."""
import hashlib,json,sys,unicodedata
from urllib.parse import urlsplit,urlunsplit,parse_qsl,urlencode

def canonical_url(value):
    u=urlsplit(value)
    if u.scheme.lower() not in ('http','https') or not u.hostname or u.username or u.password:raise ValueError('public HTTP(S) posting URL required')
    query=[(k,v) for k,v in parse_qsl(u.query,keep_blank_values=True) if not k.lower().startswith('utm_')]
    authority=u.netloc.lower()
    if (u.scheme.lower(),u.port) in (('https',443),('http',80)):authority=authority.rsplit(':',1)[0]
    return urlunsplit((u.scheme.lower(),authority,u.path or '/',urlencode(sorted(query)),''))

def normalize(data):
    seen={};rows=[];duplicates=[]
    if not isinstance(data['jobs'],list):raise ValueError('jobs must be a list')
    for i,job in enumerate(data['jobs']):
        if not isinstance(job,dict):raise ValueError('each job must be an object')
        company=job['company'];title=job['title']
        if not isinstance(company,str) or not company.strip() or not isinstance(title,str) or not title.strip():raise ValueError('company and title required')
        company_key=unicodedata.normalize('NFKC',company).casefold().strip()
        req=job.get('requisition_id');url=canonical_url(job['url']) if job.get('url') else None
        if req is not None and (not isinstance(req,str) or not req.strip()):raise ValueError('requisition_id must be a nonempty string')
        if req is None and url is None:raise ValueError('requisition_id or posting URL required; title alone is ambiguous')
        identity=[company_key,'requisition',req.strip()] if req else [company_key,'url',url]
        key=hashlib.sha256(json.dumps(identity,ensure_ascii=False).encode()).hexdigest()
        record=dict(job,key=key,canonical_url=url)
        if key in seen:duplicates.append({'input_index':i,'same_identity_as':seen[key],'record':record})
        else:seen[key]=i;rows.append(record)
    claims=data.get('claims',[]);facts=data.get('facts',{})
    if not isinstance(claims,list) or not isinstance(facts,dict):raise ValueError('claims list and facts mapping required')
    audit=[]
    for c in claims:
        if not isinstance(c,dict) or not isinstance(c.get('fact_id'),str):raise ValueError('each claim needs a string fact_id')
        f=facts.get(c['fact_id'])
        supported=isinstance(f,dict) and isinstance(f.get('source'),str) and bool(f['source'].strip()) and f.get('value') is not None and type(c.get('value')) is type(f.get('value')) and c.get('value')==f.get('value')
        audit.append(dict(c,status='PASS' if supported else 'UNVERIFIED',reason='Exact value and source present' if supported else 'Missing or different candidate fact'))
    return {'jobs':rows,'duplicate_records':duplicates,'claims':audit,'semantic_claim_support':'UNVERIFIED: exact equality does not establish appropriate use','submissions':0}

if __name__=='__main__':
    try:
        with open(sys.argv[1],encoding='utf-8-sig') as f:result=normalize(json.load(f))
        print(json.dumps(result,ensure_ascii=False));sys.exit(any(c['status']!='PASS' for c in result['claims']))
    except (OSError,ValueError,KeyError,TypeError,IndexError) as e:print(json.dumps({'error':str(e)}));sys.exit(2)
