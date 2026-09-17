"""Run explicitly approved argv checks and detect stale file/definition evidence."""
import argparse,hashlib,json,os,signal,subprocess,tempfile,time
from pathlib import Path

def digest(data):return hashlib.sha256(data).hexdigest()
def definition(manifest):return digest(json.dumps(manifest,sort_keys=True,allow_nan=False).encode())
def validate(manifest):
    cwd=Path(manifest['cwd'])
    if not cwd.is_absolute() or not cwd.is_dir():raise ValueError('cwd must be an existing absolute directory')
    checks=manifest['checks'];inputs=manifest['inputs']
    if not isinstance(checks,list) or not checks or not isinstance(inputs,list) or not inputs:raise ValueError('nonempty checks and inputs required')
    ids=set()
    for c in checks:
        if not isinstance(c['id'],str) or not c['id'] or c['id'] in ids:raise ValueError('unique check ids required')
        ids.add(c['id'])
        if not isinstance(c['argv'],list) or not c['argv'] or any(not isinstance(a,str) or not a for a in c['argv']):raise ValueError('argv must be nonempty strings; no shell string')
        if not isinstance(c['expect_stdout'],str) or not c['expect_stdout']:raise ValueError('nonempty expected stdout literal required')
        timeout=c.get('timeout',30)
        if isinstance(timeout,bool) or not isinstance(timeout,(int,float)) or not 0<timeout<=600:raise ValueError('timeout must be 0..600 seconds')
    if len(inputs)!=len(set(inputs)):raise ValueError('duplicate inputs')
    return cwd.resolve()

def snapshot(manifest):
    cwd=validate(manifest);out={}
    for name in manifest['inputs']:
        if not isinstance(name,str) or not name or Path(name).is_absolute():raise ValueError('input paths must be relative')
        p=(cwd/name).resolve()
        if not p.is_relative_to(cwd) or not p.is_file():raise ValueError(f'missing or outside-cwd input: {name}')
        out[name]=digest(p.read_bytes())
    return out

def run(manifest):
    before=snapshot(manifest);results=[];cwd=validate(manifest)
    for check in manifest['checks']:
        with tempfile.TemporaryFile() as stdout, tempfile.TemporaryFile() as stderr:
            options={'creationflags':subprocess.CREATE_NEW_PROCESS_GROUP} if os.name=='nt' else {'start_new_session':True}
            started=time.time();reason=None
            try:
                child=subprocess.Popen(check['argv'],cwd=cwd,stdout=stdout,stderr=stderr,shell=False,**options)
                try:child.wait(timeout=check.get('timeout',30))
                except subprocess.TimeoutExpired:
                    reason='timeout'
                    if os.name=='nt':subprocess.run(['taskkill','/PID',str(child.pid),'/T','/F'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                    else:os.killpg(child.pid,signal.SIGKILL)
                    child.wait(timeout=10)
                rc=child.returncode
            except OSError as e:rc=None;reason=type(e).__name__
            stdout.seek(0);raw=stdout.read(1048577);stderr.seek(0);err=stderr.read(1048577)
            if len(raw)>1048576 or len(err)>1048576:reason='output exceeds 1 MiB per stream'
            matched=check['expect_stdout'] in raw.decode('utf-8',errors='replace')
            results.append({'id':check['id'],'status':'PASS' if rc==0 and matched and reason is None else 'FAIL',
                            'exit_code':rc,'expected_stdout_found':matched,'reason':reason,'stdout_sha256':digest(raw),'stderr_sha256':digest(err),'elapsed_seconds':time.time()-started})
    try:stable=before==snapshot(manifest)
    except (OSError,ValueError):stable=False
    return {'schema':1,'definition_sha256':definition(manifest),'inputs':before,'checks':results,
            'status':'PASS' if stable and all(x['status']=='PASS' for x in results) else 'FAIL','inputs_unchanged_during_run':stable,
            'scope':'Only declared files and predicates; completeness of the requirement map requires review'}

def verify(manifest,record):
    current=snapshot(manifest)
    valid=(record.get('schema')==1 and record.get('definition_sha256')==definition(manifest) and record.get('inputs')==current
           and record.get('status')=='PASS' and record.get('inputs_unchanged_during_run') is True
           and [x.get('id') for x in record.get('checks',[])]==[x['id'] for x in manifest['checks']]
           and all(x.get('status')=='PASS' and x.get('exit_code')==0 and x.get('expected_stdout_found') is True and x.get('reason') is None for x in record.get('checks',[])))
    return {'status':'PASS' if valid else 'STALE_OR_FAILED','scope':'Integrity/freshness check of a trusted local evidence record, not tamper-proof execution attestation'}

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('mode',choices=['run','verify']);p.add_argument('manifest');p.add_argument('record');a=p.parse_args()
    try:
        manifest=json.loads(Path(a.manifest).read_text(encoding='utf-8-sig'))
        if a.mode=='run':
            if Path(a.record).exists():raise ValueError('record already exists; use a new path')
            result=run(manifest)
            with open(a.record,'x',encoding='utf-8') as f:json.dump(result,f,indent=2)
        else:result=verify(manifest,json.loads(Path(a.record).read_text(encoding='utf-8-sig')))
        print(json.dumps(result));p.exit(0 if result['status']=='PASS' else 1)
    except (OSError,ValueError,KeyError,TypeError,subprocess.SubprocessError) as e:p.exit(2,str(e)+'\n')
