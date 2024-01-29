from fastapi import APIRouter, HTTPException, Query, Path
from httpx import AsyncClient
import certifi
from typing import List, Optional

router = APIRouter()

# External API endpoint
EXTERNAL_API_URL = "https://www.cbioportal.org/api"

# Server running status
@router.get("/health")
async def get_health_status():
    try:
        async with AsyncClient(verify=certifi.where()) as client:
            response = await client.get(EXTERNAL_API_URL + "/health")
        
        response.raise_for_status()
        
        external_data = response.json()
        return {"status": external_data["status"]}

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail="External API Error")

    except Exception as e:
        print(f"Internal server error: {e}")  # Log the error for debugging
        raise HTTPException(status_code=503, detail="Internal Data Registry Server Error")

@router.post("/studies/{studyId}/clinical-data/fetch")
async def fetch_clinical_data(
    studyId: str = Path(..., title="Study ID", description="e.g., acc_tcga"),
    clinicalDataType: str = Query("SAMPLE", title="Clinical Data Type", description="Type of the clinical data", regex="^(SAMPLE|PATIENT)$"),
    projection: str = Query("SUMMARY", title="Projection", description="Level of detail of the response", regex="^(ID|SUMMARY|DETAILED|META)$"),
    request_data: dict = {
        "ids": List[str],
        "attributeIds": List[str]
    }
):
    try:
        # Validate request data
        ids = request_data.get("ids", [])
        attribute_ids = request_data.get("attributeIds", [])

        # Make the request to the external API
        async with AsyncClient(verify=certifi.where()) as client:
            response = await client.post(
                f"{EXTERNAL_API_URL}/studies/{studyId}/clinical-data/fetch",
                params={
                    "clinicalDataType": clinicalDataType,
                    "projection": projection
                },
                json={
                    "ids": ids,
                    "attributeIds": attribute_ids
                }
            )

        response.raise_for_status()

        # Parse the response
        clinical_data = response.json()
        return clinical_data

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail="External API Error")

    except Exception as e:
        print(f"Internal server error: {e}")  # Log the error for debugging
        raise HTTPException(status_code=503, detail="Internal Data Registry Server Error")
