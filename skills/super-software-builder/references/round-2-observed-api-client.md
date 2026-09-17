# Observed api client

When an authorized HAR or equivalent request/response capture is supplied, identify relevant endpoints and compare actual varying requests. Derive types and a client function per observed flow. Keep observed schema separate from guessed optional fields, and verify response shapes, error handling and expired-session behavior.

For an authorized supported Electron automation surface, select the exact application, window or webview. Inspect fresh state, act on observed element references, refresh after state changes, isolate named sessions and verify the resulting state. Support depends on the actual application and host; do not assume every Electron app supports the source's mechanism. Do not automatically quit/relaunch apps, enable debug ports or bypass a blocked host surface.

Redact tokens, cookies and personal data before creating fixtures or logs. Parameterize runtime credentials; do not embed captured sessions. A capture does not authorize replay of state-changing requests. Do not export cookies, bypass browser policy, delete source files or assume a desktop automation bridge exists because an upstream example does so.

## Provenance

Round 2, vercel-labs/agent-browser, commit `8c15ff9f71ae60c7e99e66afe1e2d4b9bf414fe2`.

- https://github.com/vercel-labs/agent-browser/blob/8c15ff9f71ae60c7e99e66afe1e2d4b9bf414fe2/skill-data/derive-client/SKILL.md
- https://github.com/vercel-labs/agent-browser/blob/8c15ff9f71ae60c7e99e66afe1e2d4b9bf414fe2/skill-data/electron/SKILL.md

Original scoped synthesis from inspected primary source. Upstream software and runtime dependencies are not installed by this reference. Behavioral effectiveness remains unverified until task trials.
