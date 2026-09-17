"""Check a local skill's metadata and referenced local files. No code execution."""
import argparse,re
from pathlib import Path

def prose_only(text):
    """Ignore fenced examples when checking references, retaining real prose."""
    fence=None;out=[]
    for line in text.splitlines(keepends=True):
        m=re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$',line.rstrip('\r\n'))
        if m:
            token,rest=m.groups()
            if fence is None:fence=token
            elif token[0]==fence[0] and len(token)>=len(fence) and not rest.strip():fence=None
            continue
        if fence is None:out.append(line)
    return ''.join(out)

def validate(root):
    root=Path(root).resolve();issues=[];entry=root/'SKILL.md'
    if not entry.is_file():return ['SKILL.md missing']
    text=entry.read_text(encoding='utf-8-sig');m=re.match(r'^---\r?\n(.*?)\r?\n---(?:\r?\n|$)',text,re.S)
    if not m:return ['leading frontmatter missing']
    name=re.search(r'^name:\s*[\"\']?([a-z0-9]+(?:-[a-z0-9]+)*)[\"\']?\s*$',m[1],re.M)
    if not name or name[1]!=root.name:issues.append('frontmatter name must match directory')
    if not re.search(r'^description:\s*\S',m[1],re.M):issues.append('description missing')
    for p in root.rglob('*'):
        if p.is_symlink():issues.append(f'symlink requires separate review: {p.relative_to(root)}');continue
        if not p.is_file() or p.suffix.lower()!='.md':continue
        body=p.read_text(encoding='utf-8-sig')
        if re.search(r'^(?:<{7}|={7}|>{7})(?: |$)',body,re.M):issues.append(f'merge marker in {p.relative_to(root)}')
        prose=prose_only(body)
        targets=re.findall(r'\[[^\]]*\]\(([^)]+)\)',prose)
        targets += re.findall(r'`((?:scripts|references|assets)/[^`\s*?]+)`',prose)
        for t in set(targets):
            t=t.split('#')[0]
            if not t or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',t):continue
            resolved=(p.parent/t).resolve()
            # Backticked package paths are relative to the skill root.
            if not resolved.exists() and t.startswith(('scripts/','references/','assets/')):resolved=(root/t).resolve()
            if not resolved.is_relative_to(root) or not resolved.is_file():issues.append(f'missing/outside package reference in {p.relative_to(root)}: {t}')
    return sorted(set(issues))

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('directory');a=p.parse_args()
    try:
        issues=validate(a.directory)
        print('\n'.join(issues) if issues else 'PASS: local reference checks; host YAML validation and behavior tests still required')
        p.exit(bool(issues))
    except (OSError,ValueError) as e:p.exit(2,str(e)+'\n')
