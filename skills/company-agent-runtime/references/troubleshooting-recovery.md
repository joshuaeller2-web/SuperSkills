# Sub-master: Troubleshooting and Recovery

Use for software defects, local-system failures, authentication boundaries, runtime failures, and recovery.

## Minor methods

- **Symptom reproduction:** reach the user's actual failure with the smallest realistic probe.
- **Fault isolation:** change one variable, trace the bad value across boundaries, and rank competing causes.
- **Known-bad control:** prove the check rejects a deliberately bad input before accepting a pass.
- **Targeted repair:** change the smallest supported surface and preserve unrelated state.
- **Recovery proof:** rerun the original workflow, neighboring checks, and rollback or restart instructions.
- **Incident handoff:** package symptom, environment, evidence, attempted changes, current state, and next owner.
