# The Bootloader

See also [post on LI](https://www.linkedin.com/pulse/symbolic-programming-llms-thebootloader-aisp-andreas-schmidt-vdovf)

## Prompts

### Bootloader 1.0

"""
Load into ℛ but do not execute: 𝔸5.1.complete@2026-01-09 𝔸1.0.ears@2026-01-23 𝔸1.0.bootloader@2026-01-09
"""

"""
Raw_Signal = "Draft requirements for the Game: Rock, Paper, Scissors (2 player hand game)"
⊢ Apply 𝔸1.0.bootloader
"""

### Bootloader 2.0

"""
Load into ℛ but do not execute: 𝔸5.1.complete@2026-01-09 𝔸1.0.ears@2026-01-23 𝔸2.0.bootloader@2026-01-09
No output.
"""

"""
Task_EARSRefinement ≜ ⟨
  context: ⟦ℭ:Categories⟧,
  Raw_Signal ≜ ∅,
  goal: ⊢ EARS.generate(Raw_Signal),
  constraints: {μ_r < 0.05, δ > 0.80}
⟩
"""

"""
⊢ Apply 𝔸2.0.bootloader.Boot(Task_EARSRefinement, Raw_Signal ≜ "Draft requirements for the Game: Rock, Paper, Scissors (2 player hand game)")
"""