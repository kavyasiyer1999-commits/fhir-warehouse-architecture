## Translator Layer

This layer acts as the ETL engine of the warehouse.

It converts legacy CSV data into FHIR-compliant
Transaction Bundles using UUID-based references.

Transactional atomicity ensures no orphaned clinical data.
