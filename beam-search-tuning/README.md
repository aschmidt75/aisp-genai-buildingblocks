# Beam Search Tuning

The AISP specification contains a block called [Beam Search](https://github.com/bar181/aisp-open-core/blob/bcd1e4820c155a284ed7deca529c94ae2cd082ce/guides/advanced/02_COGNITION.md#3-search-pipeline-beam-search), which is responsible for finding the best possible answer to a question when there are many possible paths to explore and you can't afford to try all of them. 

Upload [aisp51.aisp](./aisp51.aisp), [ears.aisp](./ears.aisp) and [run-tunable-ears.aisp](./run-tunable-ears.aisp) into a new session.

The `ears_run` lets you hand over the basic requirements to be EARS-specified, plus the K and τ parameters to tune the beam search, e.g.:

```
⊢𝔸5.1.complete@2026-01-09
⊢𝔸1.0.ears@2026-01-23

s ≜ "The ATM should let users withdraw cash, handle card errors, and lock after 3 failed PINs"
cfg ≜ ⟨K≔3, τ≔0.7⟩
ears_run(s, cfg)
```

Above returns semi-formal output with high readability. The following returns full AISP:

```
⊢𝔸5.1.complete@2026-01-09
⊢𝔸1.0.ears@2026-01-23

⟦Λ:Call⟧{ 
    s ≜ "The ATM should let users withdraw cash, handle card errors, and lock after 3 failed PINs" 
    cfg ≜ ⟨K≔2, τ≔1.0⟩ 
    result ≜ ears_run(s, cfg) 
}
```

- Higher K means more requirements in the output (= more beams to follow)
- Higher τ means the requirement sentences are more complex
- Lower τ means sentences are shorter, more precise.