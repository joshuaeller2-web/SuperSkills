# Candidate facts and job records

Replace `<skill-dir>` with the absolute directory containing this skill's SKILL.md. Keep the script path quoted; input paths refer to your task workspace. Use an available Python 3.10+ interpreter.

`python "<skill-dir>/scripts/job_records.py" input.json` normalizes local records and checks explicit claim values:

```json
{"jobs":[{"company":"Example","title":"Engineer","requisition_id":"REQ-12","url":"https://example.com/jobs/12?utm_source=mail"}],"facts":{"remote":{"value":"required","source":"user preference, 2026-09-08"}},"claims":[{"fact_id":"remote","value":"required"}]}
```

Identity uses normalized company plus exact requisition ID; without an ID it uses the posting URL. Requisition IDs remain case-sensitive; company names are normalized separately. Default HTTP/HTTPS ports are normalized. Only utm parameters and fragments are removed; other query parameters may identify different requisitions. Company/title alone is rejected. Duplicate records stay in a separate list with their complete original fields so differences can be reconciled. Organization aliases and redirects need human/agent reconciliation; do not assume this detects every duplicate.

Candidate facts retain their source and original specificity. A matching stored value is a literal evidence check, not proof that using it in a sentence is truthful. A preference for remote work does not establish remote employment history. Missing evidence produces UNVERIFIED and exit 1. Invalid input exits 2. No form is filled and no application is submitted.

For an authorized application, use the exact profile-supported answer or leave it unresolved. Never use Yes/No defaults for experience, languages, disability, sponsorship or consent. Match question meaning, not substrings such as rag inside storage. Keep prepared, submission-unverified and observed-submitted states distinct. Derive learning gaps from real target roles without scoring unknown experience as zero.

Company matching preserves internal whitespace and punctuation. Reconcile padded names and organization aliases separately; conservative matching may leave duplicates for review.
