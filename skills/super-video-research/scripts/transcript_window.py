"""Select supplied transcript intervals before limiting. No network or transcription."""
import argparse,json,math

def number(value):
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not math.isfinite(value):raise ValueError('finite numeric time required')
    return value

def select(data,start=0,end=None,limit=None):
    start=number(start)
    if start<0 or (end is not None and number(end)<=start):raise ValueError('require 0 <= start < end')
    if limit is not None and (isinstance(limit,bool) or not isinstance(limit,int) or limit<1):raise ValueError('limit must be positive integer')
    raw=data['segments']
    if not isinstance(raw,list):raise ValueError('segments must be a list')
    matches=[]
    for s in raw:
        offset,duration=number(s['offset']),number(s['duration'])
        if offset<0 or duration<0 or not isinstance(s['text'],str):raise ValueError('invalid segment')
        if (offset+duration>start or duration==0 and offset>=start) and (end is None or offset<end):matches.append(s)
    matches.sort(key=lambda s:s['offset']);returned=matches if limit is None else matches[:limit]
    return {'identity':data.get('identity'),'identity_status':'available' if data.get('identity') else 'UNAVAILABLE: source identity not supplied',
            'window':{'start':start,'end':end},'input_segments':len(raw),'matched_segments':len(matches),
            'returned_segments':len(returned),'truncated':len(returned)<len(matches),
            'source_coverage':data.get('source_coverage','UNVERIFIED: completeness of supplied transcript unknown'),
            'segments':returned}

def pacing(duration,cuts):
    duration=number(duration)
    if duration<=0:raise ValueError('duration must be positive')
    if not isinstance(cuts,list):raise ValueError('cuts must be a list')
    cuts=[number(x) for x in cuts]
    if cuts!=sorted(set(cuts)) or any(x<=0 or x>=duration for x in cuts):raise ValueError('cuts must be distinct ordered internal boundaries, excluding zero/end')
    boundaries=[0]+cuts+[duration]
    return {'internal_cuts':len(cuts),'cuts_per_minute':len(cuts)*60/duration,'shot_durations':[b-a for a,b in zip(boundaries,boundaries[1:])],
            'coverage':'Measured only if all supplied boundaries are observed and complete'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input');p.add_argument('--start',type=float,default=0);p.add_argument('--end',type=float);p.add_argument('--limit',type=int);p.add_argument('--pacing',action='store_true');a=p.parse_args()
    try:
        with open(a.input,encoding='utf-8-sig') as f:data=json.load(f)
        print(json.dumps(pacing(data['duration'],data['cuts']) if a.pacing else select(data,a.start,a.end,a.limit),ensure_ascii=False))
    except (OSError,ValueError,KeyError,TypeError) as e:p.exit(2,str(e)+'\n')
