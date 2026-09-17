# Agent routing

Use this reference only after Company OS or delegated agent work is active.

## Decision order

1. **Direct named role:** keep the named role if its charter owns the requested deliverable.
2. **Clear single function:** choose the narrowest specialist in `organization.json` whose purpose matches the output.
3. **Manager coordination:** choose the department manager when the work contains several related specialist outputs.
4. **Cross-department or unclear intake:** route first to `company-chief-of-staff`.
5. **Independent acceptance:** route the finished evidence to `company-independent-verifier` or the applicable audit/security role. The author does not independently grade its own work.

## Examples

- A reproducible application defect: `evidence-debugging -> company-debugging-specialist -> Troubleshooting and Recovery / Symptom reproduction -> company-independent-verifier`.
- A recurring machine-health task: `standing-jobs -> company-systems-administrator -> Operations and Maintenance / Preventive maintenance -> company-run-monitor`.
- An unclear request involving finance and software: `stack-router -> company-chief-of-staff -> Assignment Dispatch / Intake shaping -> named department owner`.

The role charter remains authoritative. These examples demonstrate routing shape; they do not prove that an adapter is loaded or authorize execution.
