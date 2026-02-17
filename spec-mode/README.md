# Specification Mode

This part demonstrates how to enter AISP specification mode for a defined target, and how to formulate it.

Examples are for KiloCode mode

Start with loading AISP 5.1, followed by the specification mode AISP:
```
load @/spec-mode/aisp51.aisp @/spec-mode/spec.aisp
no_execute no_output
```

Then, referencing both specs, followed by the context you want to have translated to AISP:

```
𝔸5.1.complete@2026-01-09 𝔸5.1.spec@2026-02-17
An address consists of name, street address, additional street address, Zip, City and Country
```

or, more complex:

```
𝔸5.1.complete@2026-01-09 𝔸5.1.spec@2026-02-17
All users with a sign-in risk score of 0.5 or higher are required to use MFA unless the request originates from a trusted device.
```

If you're using a coding agent, you can add mode-specific custom instructions, e.g. 

```
load @/spec-mode/aisp51.aisp @/spec-mode/spec.aisp
no_execute no_output.
Ask for Objective to spec out and file to write to.
```

If possible, remove system context to save tokens. You don't need it, AISP has little ambiguity.