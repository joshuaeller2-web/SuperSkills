---
name: workbench
description: "Diagnose Windows shell, executable-path, encoding and environment problems. Use when commands fail because of the execution surface; does not automatically reconfigure WSL, credentials or security controls."
---

# workbench

Identify the actual shell and working directory, intended executable and observed failure. Reproduce a bounded failure before changing environment settings. Check quoting, PATH or shim resolution, input/output encoding, line endings and path separators in that order when relevant.

For a synchronous PowerShell native preflight, prefer `& $Executable @Arguments` to avoid `Start-Process -ArgumentList` rejoining a complex Python `-c` string without the required quoting. Keep asynchronous server launches separate and test their argument quoting explicitly. Reference environment-variable names containing parentheses with braces, for example `${env:ProgramFiles(x86)}`. Verify the resolved executable and actual native invocation; a source-string assertion or successful ZIP build does not prove the Windows launcher runs.

Use the intended interpreter explicitly. Keep file mutations within one shell and use literal paths. Verify resolved targets before recursive moves; preserve collisions and originals. Do not pass constructed destructive commands across PowerShell, cmd and WSL.

For native-launcher negative tests, allocate independent ports and prove the expected fixture owns its listener before invoking the subject. Retain fixture stderr and require bounded readiness, rather than sleeping and assuming it bound: a surviving positive-case server can short-circuit later probes into an already-running branch. Classify failed fixture setup as harness failure/UNVERIFIED, not product FAIL or PASS. Treat a separate interpreter import probe as evidence only for that invocation, not a launcher with a different working directory.

When Python starts but the listener PID differs from the retained launch handle, inspect Windows venv redirector and launcher-child behavior before labeling the listener foreign. Bind a legitimate child to verified launch ancestry, process creation time, expected executable and the startup instance; never replace that proof with a same-name process or health marker. Preserve separate source, extracted-file and ZIP hashes when a crashed attempt leaves unbuilt edits.

Bound readiness by elapsed time, not only an iteration count multiplied by a sleep. Measure ownership and network-probe duration separately; repeated native process/TCP queries can exceed the apparent wait budget. Preserve the original timeout failure and diagnose it rather than declaring a longer retry a fix.

For cleanup, retain the owned process handle or revalidate PID, creation time, executable and ancestry immediately before stopping it. A recorded PID or current port owner alone is not authorization. Close the exact newly owned browser window, not a shared browser process. Require owned-window content/visual evidence for UI launch; a nonempty full-desktop screenshot does not prove the intended UI and may disclose unrelated content.

For requested isolation, inspect mounts, credentials, network access and real host support. Propose or implement the authorized boundary and test it with a harmless denied-access control. Merely disabling automount is not proof of comprehensive isolation. Do not rewrite WSL settings, install guards, terminate distributions or relocate repositories during ordinary shell debugging.

Keep secret values out of source, logs and tool output. Test redaction with synthetic markers rather than printing real environment secrets. Report command, exit code and remaining failure boundary.

Read [draft provenance and incorporated methods](references/draft-methods.md) when revising these methods.
