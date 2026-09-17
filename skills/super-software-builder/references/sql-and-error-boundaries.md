# SQL provenance and production errors

## Before constructing or executing SQL
Trace where SQL text, identifiers and values originate. Keep user, URL, stored snippet and model-generated SQL untrusted. Database storage alone does not establish trust. Parameterize values; use appropriate identifier quoting or allowlists separately. Do not silence provenance errors with a cast or automatically run externally influenced SQL during render, queries, effects or background loading.

Where an application intentionally supports arbitrary SQL, use its explicit reviewed execution flow with existing authorization and a visible query. Provenance is separate from authorization and destructive impact: even trusted text may perform an unauthorized or destructive operation. Do not transplant Supabase Studio's owner-database catalog assumptions into other applications. Do not impose a new confirmation on already authorized parameterized operations.

## Production errors
Use the existing central error handling path. Return client-safe errors and a correlation identifier. Exercise an error response and inspect it for stack traces, internal paths and secrets. Retain useful internal diagnostics under the application's access and redaction rules. Do not log credentials or personal data simply because a checklist says to log full details.

## Provenance and limits
- supabase/supabase, commit `d439ba57f4228785ca34a62828b637009a7cbab6`, `.agents/skills/safe-sql-execution/SKILL.md`: https://github.com/supabase/supabase/blob/d439ba57f4228785ca34a62828b637009a7cbab6/.agents/skills/safe-sql-execution/SKILL.md
- thedaviddias/Front-End-Checklist, commit `30756a79b2f7d4363ac592710146c8e28fa9f1b5`, `skills/stack-trace-exposure/SKILL.md`: https://github.com/thedaviddias/Front-End-Checklist/blob/30756a79b2f7d4363ac592710146c8e28fa9f1b5/skills/stack-trace-exposure/SKILL.md

Round 1, reviewed 2026-09-14. Original synthesis, no upstream software installed. Supabase's source moved from .claude to .agents. Application-specific runtime behavior remains UNAVAILABLE until tested in that application.
