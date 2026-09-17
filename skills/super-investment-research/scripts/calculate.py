"""Local calculations from supplied assumptions; no market data or brokerage access."""
import argparse,datetime,json,math

def finite(x):
    if isinstance(x,bool) or not isinstance(x,(int,float)) or not math.isfinite(x):raise ValueError('finite numeric input required')
    return x

def valuation(d):
    if any(k not in d for k in ('profit','pe','net_debt','shares')):raise ValueError('valuation requires profit, pe, net_debt (0 for equity PE), and shares')
    profit,pe,debt,shares=[finite(d[k]) for k in ('profit','pe','net_debt','shares')]
    if pe<0 or shares<=0:raise ValueError('nonnegative PE and positive shares required')
    # Earnings belong to equity. Net debt is not subtracted from a PE valuation.
    if debt!=0:raise ValueError('PE values equity directly: use net_debt=0; do not subtract debt twice')
    return {'equity_value':profit*pe,'per_share':profit*pe/shares,'basis':'Equity earnings x PE; inputs must use matching units and diluted shares'}

def terminal_pe(d):
    g,r,roic=[finite(d[k]) for k in ('growth','discount_rate','roic')]
    if roic<=0 or r<=g or g>=roic:raise ValueError('requires ROIC>0, discount>growth and growth<ROIC')
    return {'terminal_pe':(1-g/roic)/(r-g),'basis':'Steady-state reinvestment model; assumptions, not a market price'}

def position(d):
    equity,risk,entry,stop=[finite(d[k]) for k in ('equity','risk_fraction','entry','stop')]
    if equity<=0 or not 0<=risk<=1 or not 0<=stop<entry:raise ValueError('long-only: equity>0, risk 0..1, 0<=stop<entry')
    shares=min(math.floor(equity*risk/(entry-stop)),math.floor(equity/entry))
    return {'shares':shares,'planned_loss_at_stop':shares*(entry-stop),'cash_required':shares*entry,'limitations':'Long-only, no leverage, fees or gap/slippage allowance; stop price is not guaranteed'}

def xirr(d):
    flows=d['cashflows']
    if not isinstance(flows,list) or len(flows)<2:raise ValueError('at least two dated cash flows required')
    parsed=sorted((datetime.date.fromisoformat(x['date']),finite(x['amount'])) for x in flows)
    first=parsed[0][0]
    if parsed[0][1]>=0 or any(amount<0 or date<=first for date,amount in parsed[1:]) or not any(amount>0 for _,amount in parsed[1:]):raise ValueError('supported: one initial negative flow, later nonnegative flows with at least one positive')
    def npv(rate):
        total=parsed[0][1]
        for date,amount in parsed[1:]:
            exponent=-(date-first).days/365*math.log1p(rate)
            total+=amount*math.exp(exponent) if exponent<700 else math.inf
        return total
    low=-0.999999999;high=1.0
    while npv(high)>0 and high<1e9:high=high*2+1
    if npv(low)<0 or npv(high)>0:raise ValueError('root outside supported numeric bracket')
    for _ in range(200):
        mid=(low+high)/2
        if npv(mid)>0:low=mid
        else:high=mid
    rate=(low+high)/2
    return {'annualized_return':rate,'npv_residual':npv(rate),'day_count':'ACT/365','basis':'Dated cash-flow IRR, conventional sign pattern only'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('mode',choices=['valuation','terminal-pe','position','xirr']);p.add_argument('input');a=p.parse_args()
    try:
        with open(a.input,encoding='utf-8-sig') as f:data=json.load(f)
        print(json.dumps({'mode':a.mode,'result':{'valuation':valuation,'terminal-pe':terminal_pe,'position':position,'xirr':xirr}[a.mode](data)},allow_nan=False))
    except (OSError,ValueError,TypeError,KeyError,OverflowError) as e:p.exit(2,str(e)+'\n')
