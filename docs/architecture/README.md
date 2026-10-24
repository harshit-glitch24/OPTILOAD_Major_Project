# OptiLoad 3D — Architecture Documentation

This folder contains the architecture reference for **OptiLoad 3D / LogiLoad India**. The diagrams are logical views intended for project reviews, onboarding, and technical viva discussions; they do not imply that every subsystem is independently deployed or production-validated.

## Documents

- [System Architecture](system-architecture.md) — layers, component responsibilities, and integration boundaries.
- [Module Map](module-map.md) — major repository modules and their relationships.
- [Workflow Diagrams](workflows.md) — cargo packing, multimodal routing, and request lifecycle.

## Reading order

1. Start with the system architecture to understand the major layers.
2. Use the module map to locate corresponding code.
3. Read the workflow diagrams to follow how key user tasks move through the application.
4. Read the repository's [Reality Gap Report](../../REALITY_GAP_REPORT.md) before describing experimental or simulated features as live capabilities.

## Architecture conventions

- **Solid logical connections** show the conceptual direction of data or requests, not necessarily a synchronous network call.
- **External services** may be unavailable, rate-limited, or require configuration.
- **Synthetic data, heuristics, experimental ML policies, and simulated telemetry** must be labelled as such in demonstrations and evaluation reports.
- This documentation should be updated when component boundaries or runtime behavior change.
