from fastapi import APIRouter, HTTPException, Path, Query, HTTPException
from httpx import AsyncClient

app = APIRouter()

# External API endpoint
EXTERNAL_API_URL = "https://www.cbioportal.org/api"


# Server running status
@app.get("/health")
async def get_health_status():
    try:
        async with AsyncClient() as client:
            response = await client.get(EXTERNAL_API_URL)
        response.raise_for_status()
        
        external_data = response.json()
        return {"external_data": external_data}

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail="External API Error")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")

# # Treatments
# @app.post("/api/treatments/sample")
# def get_treatment_sample():
#     return {"message": "Treatment created for sample"}

# @app.post("/api/treatments/patient")
# def create_treatment_patient():
#     return {"message": "Treatment created for patient"}

# # Add other treatment routes...

# # Clinical Data
# @app.post("/api/studies/{studyId}/clinical-data/fetch")
# def fetch_clinical_data(studyId: int, query_param: str = Query(None)):
#     return {"studyId": studyId, "query_param": query_param}

# # Add other clinical data routes...

# # Studies
# @app.post("/api/studies/tags/fetch")
# def fetch_study_tags():
#     return {"message": "Fetching study tags"}

# # Add other study routes...

# # Samples
# @app.post("/api/samples/fetch")
# def fetch_samples():
#     return {"message": "Fetching samples"}

# # Add other sample routes...

# # Sample Lists
# @app.post("/api/sample-lists/fetch")
# def fetch_sample_lists():
#     return {"message": "Fetching sample lists"}

# # Add other sample list routes...

# # Patients
# @app.post("/api/patients/fetch")
# def fetch_patients():
#     return {"message": "Fetching patients"}

# # Add other patient routes...

# # Mutations
# @app.post("/api/mutations/fetch")
# def fetch_mutations():
#     return {"message": "Fetching mutations"}

# # Add other mutation routes...

# # Molecular Data
# @app.post("/api/molecular-profiles/{molecularProfileId}/molecular-data/fetch")
# def fetch_molecular_data(molecularProfileId: int):
#     return {"molecularProfileId": molecularProfileId}

# # Add other molecular data routes...

# # Add other routes...

# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)
