"""Collect supplied participant evidence; never invent seats, votes or consensus."""
import json,sys

def collect(data):
    seats=data['seats']
    if not isinstance(seats,list) or not seats:raise ValueError('nonempty seats list required')
    ids=set();available=[];unavailable=[]
    for seat in seats:
        name=seat['id']
        if not isinstance(name,str) or not name or name in ids:raise ValueError('seat identifiers must be unique nonempty strings')
        ids.add(name)
        if seat['status'] not in ('completed','failed','unavailable'):raise ValueError('invalid seat status')
        if seat['status']=='completed':
            for field in ('source','position','strongest_objection','reversing_evidence'):
                if not isinstance(seat.get(field),str) or not seat[field].strip():raise ValueError(f'completed seat requires {field}')
            available.append(seat)
        else:unavailable.append(seat)
    return {'available_views':available,'unavailable_seats':unavailable,'independence':'UNVERIFIED: supplied source labels are not proof of independent execution',
            'consensus':'NOT COMPUTED','next_step':'Compare objections and reversing evidence; verify factual disputes before synthesis'}

if __name__=='__main__':
    try:
        with open(sys.argv[1],encoding='utf-8-sig') as f:result=collect(json.load(f))
        print(json.dumps(result,ensure_ascii=False));sys.exit(not result['available_views'])
    except (OSError,ValueError,KeyError,TypeError,IndexError) as e:print(json.dumps({'error':str(e)}));sys.exit(2)
