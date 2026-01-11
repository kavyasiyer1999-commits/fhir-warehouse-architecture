## Infrastructure Layer

This layer represents the warehouse storage layer.

A HAPI FHIR server is instantiated using Docker to ensure:
- Environment consistency
- Portability across systems
- Stateful storage for FHIR resources

Port mapping (8080:8080) exposes the FHIR REST API to the host machine.
Infrastructure layer for FHIR warehouse
