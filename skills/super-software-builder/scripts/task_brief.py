"""Print one numbered Markdown task, excluding misleading headings in fences."""
import argparse, re
from pathlib import Path

def extract(text, number):
    if number < 1: raise ValueError('task number must be positive')
    lines = text.splitlines(keepends=True); fence = None; headings = []
    for i, line in enumerate(lines):
        m = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line.rstrip('\r\n'))
        if m:
            token, rest = m.groups()
            if fence is None: fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not rest.strip(): fence = None
            continue
        if fence: continue
        h = re.match(r'^ {0,3}(#{1,6})\s+(.+)', line)
        if h: headings.append((i, len(h[1]), h[2].strip()))
    matches = [(i, level) for i, level, title in headings if re.match(rf'^Task\s+{number}(?![\w]|[.]\d)(?:\b|:)', title, re.I)]
    if len(matches) != 1: raise ValueError(f'expected one Task {number} heading; found {len(matches)}')
    start, level = matches[0]
    end = next((i for i, depth, _ in headings if i > start and depth <= level), len(lines))
    return ''.join(lines[start:end])

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('plan');p.add_argument('number',type=int);a=p.parse_args()
    try: print(extract(Path(a.plan).read_text(encoding='utf-8-sig'), a.number), end='')
    except (OSError,ValueError) as e: p.exit(2,str(e)+'\n')
