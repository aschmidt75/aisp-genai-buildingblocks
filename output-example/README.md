# Output Control for AISP

This folder contains examples for manipulating the output of the AISP process. Depending on the use case, inputs can be prose text or structured AISP. The same applies for the output format.

What follows is some working practises of controlling the output.

# Base example: No output format indication

[output1.aisp](./output1.aisp) is the base specification for an address-parsing functionality. It tries to parse US addresses with
recipient names, street names (including parts), states, zip etc. 

For running the example, set the coding agent to "Ask-only" mode, or run in non-agent UIs.

```
@output-example/aisp51.aisp @output-example/output1.aisp ingest, no_Exec
```

Feeding a concrete sample address:

```
⊢𝔸1.0.address@2026-04-05
James Kirk
17771 NE 90th St
Redmond, Washington(WA), 98052
```

returns with a mix on prose, execution traces and AISP snippets - but not a full document.

# Enforce AISP document as output


[output2.aisp](./output2.aisp) is a refactored version of `output1.aisp`. It contains several occurences where the output format is directed towards a full AISP document (the spec refers to this as 𝔻oc), e.g. lines 50-52:

```
  ;; Output document type — every emitted response must conform
  Output ≜ 𝔻oc                             ;; valid AISP document
  𝔻oc    ≜ Σ(b⃗:Vec n 𝔅)(π:Γ⊢wf(b⃗))      ;; proof-carrying code
```

Running this:

```
@output-example/aisp51.aisp @output-example/output2.aisp
```

with a different adress:

```
⊢𝔸1.1.address@2026-04-05
James T. Kirk
14100 Joe Hamilton Rd
Grand Bay, Alabama(AL), 36541
```

returns AISP-only:

```
𝔸1.1.address@2026-04-05 γ≔postal.address.decomposition ρ≔⟨address,street,unit,locality,region,postal⟩ ⊢ND∧ΠΣ∧CAT

⟦Ε⟧⟨ 
    δ≜0.81 
    φ≜96 
    τ≜◊⁺⁺ 
    State≜⊤ 
    Δ⊗λ(Address,Output)≜3 
    ⊢ND 
    ⊢Binding:Post(Address)⊆Pre(Output)⇒Δ⊗λ≡3 
    ⊢Example: input≜"James T. Kirk\n14100 Joe Hamilton Rd\nGrand Bay, AL 36541" 
    recipient≜⟨given≜"James T.",family≜"Kirk"⟩ 
    street≜⟨
        num≜14100,
        dir≜∅,
        name≜"Joe Hamilton",
        suffix≜"Rd"
    ⟩ 
    unit≜∅ 
    city≜"Grand Bay"; 
    state≜"AL"; 
    zip≜"36541" 
    output≜toDoc(parse(input))∈Output; 
    State≜⊤ 
    ⊢Ambig<0.02 
⟩
```

# Enforce results in specific blocks

The last run returned all outputs in the evidence section. We can also choose to have the output in an individual "Results" blocks. 

[output3.aisp](./output3.aisp) is a refactored version of `output2.aisp`. It extends the functions block with lines 226-229 to specifially format the output:

```
  output ≜ λa.
    let v = validate(a) in
    v ≡ ⊘ → ⊥
    | ⟦Ω⟧{context}∘⟦ℜ:Result⟧⟨content≜render(a)⟩∘⟦Χ⟧{errors}∘⟦Ε⟧⟨proof≜wf(a), tier≜v⟩  
```

The above reads like "let the output be the processing of results a, where v is the validation of it. If validation is empty (`⊘` means not validated), return false (`⊥`) otherwise return the product of Context, **⟦ℜ:Result⟧⟨content≜render(a)⟩** (which will be the structured result), errors and the evidence section:

```
@output-example/aisp51.aisp @output-example/output3.aisp
```

```
⊢𝔸1.2.address@2026-04-05

James T. Kirk
263 Stonington Dr
Augusta, Georgia(GA), 30907
```

yields

```
𝔸1.2.address@2026-04-05
γ≔postal.address.decomposition
ρ≔⟨address,street,locality,region,postal⟩
⊢ND∧ΠΣ

⟦ℜ:Result⟧⟨
  recipient ≜ ⟨given≜"James", family≜"T. Kirk"⟩
  street    ≜ ⟨num≜263, dir≜∅, name≜"Stonington", suffix≜"Dr"⟩
  unit      ≜ ∅
  city      ≜ "Augusta"
  state     ≜ "GA"
  zip       ≜ "30907"
  render    ≜ "James T. Kirk\n263 Stonington Dr\nAugusta, GA 30907"
⟩

⟦Χ:Errors⟧⟨
  ε_state_case⇒recovered; "Georgia(GA)"→"GA"
⟩

⟦Ε⟧⟨
  δ≜0.81
  φ≜97
  τ≜◊⁺⁺
  State≜⊤
  Δ⊗λ(Address,Output)≜3
  ⊢wf(a)
  ⊢Ambig<0.02
  ⊢Γ:Rules[8/8]
  ⊢Χ:ε_state_case→recovered∎
⟩
```

Here we can parse the output from the `⟦ℜ:Result⟧` tuple.