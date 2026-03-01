# AISP MCP bridge example

This example bridges an AISP specification to an MCP server.
It uses the sample [weather service MCP](https://github.com/modelcontextprotocol/python-sdk/blob/main/examples/mcpserver/weather_structured.py) from Python SDK on modelcontextprotocol.

Start with the AISP specifications of AISP51 and the weather service:

```
@/aisp-mcp-bridge/aisp51.aisp @/aisp-mcp-bridge/weather-service.aisp
ingest no_exec no_output
```

Formulate a request. We could pass the name of a city here, but let's leave this open to the user (ψ_user:𝕊).

```
(...)
;; ─── Ω: META ───
⟦Ω:Meta⟧{
  ;; Context: Import from weather.mcp.service
  ctx≔𝔸5.1.weather@2026-02-20[γ≔weather.mcp.service]
  ∀city:𝕊.∃!wd:WeatherData.request(city)≡wd
}

⟦Σ:Types⟧{
  Input≜ψ_user:𝕊
  Output≜𝔻oc:AISP
}

;; ─── Λ: FUNCTIONS ───
⟦Λ:Functions⟧{
  request:𝕊→WeatherData
  request≜λcity.get_weather(city)
}

(...)
```

Check if the weather request conforms to the service:
```
𝔸5.1.complete@2026-01-09 𝔸5.1.weather@2026-02-20
@/aisp-mcp-bridge/weather-request-minimal.aisp 
⊢ 𝔸5.1.weather@2026-02-20
```

Run the request. The Agent will ask for the city name, ask the MCP server and return the weather data:
```
Run(𝔸5.1.weather_request@2026-02-20) ≫ ⟦Ω⟧{State ≔ ⊤} ≫ ⊢execute
```

We can improve the weather request to output an AISP pocket structure, see [weather-request-pocket.aisp](./weather-request-pocket.aisp)
Open a new context, put the 3 specs in, then:

```
Run(𝔸5.1.weather_pocket@2026-02-20) ≫ ⟦Ω⟧{State ≔ ⊤} ≫ ⊢execute
```

This will first realize the connection to the MCP server, then the missing city name (so far):

```
`⊢execute` — `Run(𝔸5.1.weather_pocket)` requires a `city:𝕊` input. No `ψ_user` was provided in the invocation.

`ε_empty≜⟨len(city)≡0,Error⟨"City name required",400⟩⟩`

Invoking [`mcp--aisp___mcp___bridge--get_weather`](aisp-mcp-bridge/src/weather_server.py) requires a concrete `city`. Provide `city:𝕊` to proceed:
```

The agent opens up an interactive dialog to ask for the city. Once supplied it forwards to the MCP server (needs approval to run), and outputs the result as AISP: 

```
Run(𝔸5.1.weather_pocket@2026-02-20) ⊢ ◊⁺

𝒫{Tokyo}≜⟨
  ℋ≔⟨id≔SHA256(𝒩.def), V≔Signal(wd), f≔0x0000000000000000⟩,
  ℳ≔⟨aff≔∅, conf≔0.95, tag≔{"weather","mcp","structured"}, use≔0⟩,
  𝒩≔⟨
    def≔"⟨temperature≔21.5,humidity≔55.0,condition≔\"partly cloudy\",wind_speed≔12.3,location≔\"Tokyo\",timestamp≔\"2026-03-01T11:36:51.830186\"⟩",
    ir≔∅, wa≔∅, σ≔sign(def)
  ⟩
⟩

⟦Ε⟧⟨
δ≜0.88
τ≜◊⁺
⊢get_weather("Tokyo")→WeatherData:⊤
⊢ValidTemp:21.5≥-273.15∎
⊢ValidHumidity:55.0∈[0,100]∎
⊢ValidWindSpeed:12.3≥0∎
⊢pocket:ℋ∧ℳ∧𝒩∎
⊢immutability:∂𝒩⇒∂ℋ.id∎
⊢content_addressing:ℋ.id≡SHA256(𝒩)∎
⟩
```

∎


