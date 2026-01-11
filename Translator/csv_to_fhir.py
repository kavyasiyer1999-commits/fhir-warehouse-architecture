import uuid
import json

# Generate UUID for patient
patient_uuid = str(uuid.uuid4())

# Create Patient resource
patient = {
    "resourceType": "Patient",
    "id": patient_uuid,
    "gender": "male",
    "birthDate": "1990-01-01"
}

# Create FHIR Transaction Bundle
bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": [
        {
            "fullUrl": f"urn:uuid:{patient_uuid}",
            "resource": patient,
            "request": {
                "method": "POST",
                "url": "Patient"
            }
        }
    ]
}

# Output bundle
print(json.dumps(bundle, indent=2))
