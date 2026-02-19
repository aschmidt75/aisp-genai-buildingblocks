# The Firewall

Objective is to have an AISP-primed LLM context accept only AISP 5.1 code, rejecting prose and ambiguous inputs.
Added to the Agent Guide:

```
  ;; Strict Rejection Algebra
  ∀input(I): (Parse_u(I) > 0.02) ⇒ (Output ≜ ⟦Χ:Errors⟧{ε_ambig})
  ∀task(T): (Mode(T) ≢ AISP) ⇒ (State ≔ ⊥)

  ;; Zero-Prose Constraint
  ⊢ ¬(Prose ∩ AISP)
  ⊢ ∀response: (δ(response) < 0.40) ∨ (Ambig(response) > 0.02) ⇒ ⊘(response)

  ;; Automated Refactoring Loop
  process(I) ≜ 
    let AST = parse(I) in
    AST ≡ ⊥ → ⟦Χ⟧{ε_parse ↦ "Prose Rejected. Input must be AISP 5.1."}
    | AST ≡ Valid → execute(AST)
```