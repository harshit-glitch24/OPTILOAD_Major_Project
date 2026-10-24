# Core Workflow Diagrams

These diagrams document the principal logical workflows at a high level. They describe the intended flow through the application and should be checked against the relevant code whenever implementation changes.

## 1. General request lifecycle

```mermaid
sequenceDiagram
    actor User
    participant UI as React UI
    participant API as FastAPI
    participant SVC as Domain / ML Service
    participant DATA as Database / Model / Provider

    User->>UI: Enter request details
    UI->>UI: Validate client-side inputs
    UI->>API: Send API request when applicable
    API->>API: Validate request schema
    API->>SVC: Dispatch to relevant operation
    SVC->>DATA: Read required data or call provider
    DATA-->>SVC: Return data / provider response
    SVC-->>API: Computed result or error
    API-->>UI: Structured response
    UI-->>User: Display result
```

## 2. Cargo packing workflow

```mermaid
flowchart TD
    A([Start]) --> B[Select cargo space or transport mode]
    B --> C[Enter item dimensions, quantities and relevant weights]
    C --> D{Input validation passes?}
    D -- No --> E[Show validation message]
    E --> C
    D -- Yes --> F[Run configured packing algorithm]
    F --> G[Generate feasible candidate placements]
    G --> H[Apply implemented geometric constraints]
    H --> I[Calculate placement and utilization summaries]
    I --> J[Render 3D packing result]
    J --> K{User wants to revise inputs?}
    K -- Yes --> C
    K -- No --> L([Review result])
```

**Important:** the exact constraints enforced depend on the selected implementation. A rendered result is not proof of certified stability, axle-load compliance, or safe operational loading.

## 3. Multimodal routing workflow

```mermaid
flowchart TD
    A([Route request]) --> B[Choose origin, destination and transport mode]
    B --> C{Transport mode}
    C -->|Road| D[Request road route from configured routing service]
    C -->|Air| E[Compute geodesic path and use available wind context]
    C -->|Sea| F[Calculate route over maritime route graph]
    D --> G[Normalize route output]
    E --> G
    F --> G
    G --> H[Render route and available summary]
    H --> I[User reviews route]
```

## 4. Prediction / AI-assisted analysis workflow

```mermaid
flowchart TD
    A([Analysis request]) --> B[Validate and normalize input]
    B --> C[Select configured model or analysis module]
    C --> D{Required model/data/provider available?}
    D -- No --> E[Return unavailable/error/fallback state]
    D -- Yes --> F[Run inference or analysis]
    F --> G[Attach available result context]
    G --> H[Display output with limitations]
    H --> I([Human review])
```

The AI/ML modules have different levels of maturity. Some training data is synthetic, some optimization policies are hybrid/heuristic, and some telemetry is simulated; see [REALITY_GAP_REPORT.md](../../REALITY_GAP_REPORT.md) before interpreting outputs as validated operational predictions.

## 5. External integration boundary

```mermaid
flowchart LR
    APP["OptiLoad Application"] --> ADAPTER["Feature-specific adapter / client"]
    ADAPTER --> CHECK{"Provider configured and reachable?"}
    CHECK -- Yes --> PROVIDER["External provider"]
    PROVIDER --> NORMALIZE["Normalize response"]
    NORMALIZE --> UI["Display result"]
    CHECK -- No --> DEGRADED["Show unavailable state or supported fallback"]
    DEGRADED --> UI
```

Provider errors, network failure, quota limits, and stale data should be handled explicitly. A fallback should not silently be presented as live external data.
