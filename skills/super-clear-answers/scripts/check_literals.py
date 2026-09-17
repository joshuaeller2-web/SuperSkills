"""Check explicitly supplied literal invariants; does not judge semantic fidelity."""
import json, sys

def check(data):
    answer, required = data['answer'], data['required']
    if not isinstance(answer, str) or not isinstance(required, list) or not required:
        raise ValueError('answer must be text and required a nonempty list of strings')
    if any(not isinstance(x, str) or not x for x in required):
        raise ValueError('required literals must be nonempty strings')
    missing = [x for x in dict.fromkeys(required) if x not in answer]
    return {'literal_status': 'FAIL' if missing else 'PASS', 'missing': missing,
            'semantic_fidelity': 'UNVERIFIED'}

if __name__ == '__main__':
    try:
        with open(sys.argv[1], encoding='utf-8-sig') as f: result = check(json.load(f))
        print(json.dumps(result, ensure_ascii=False)); sys.exit(bool(result['missing']))
    except (ValueError, KeyError, TypeError, OSError, IndexError) as e:
        print(json.dumps({'error': str(e)})); sys.exit(2)
