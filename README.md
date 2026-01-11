# FHIR Warehouse Architecture

This project implements a stateful, validated FHIR-based data warehouse.

## Architecture Layers
- Infrastructure: Dockerized HAPI FHIR server
- Rulebook: FHIR Shorthand profiles and ConceptMaps
- Translator: CSV to FHIR transaction bundle conversion
- Documentation: Logical design and mapping artifacts

## Key Design Principles

### Container Advantage
Docker eliminates dependency conflicts and ensures a consistent runtime
environment across different machines.

### Semantic Integrity
ConceptMaps are used to translate legacy magic strings into
FHIR-compliant codes using standardized terminology.

### Transactional Atomicity
FHIR Transaction Bundles ensure atomic creation of resources,
preventing orphaned or partial data ingestion.

## Outcome
The architecture represents a true healthcare data warehouse:
- Stateful
- Validated
- Semantically governed
- Transactionally safe
# fhir-warehouse-architecture
FHIR-based warehouse architecture using Docker, FSH, and Transaction Bundles
