import sys
import os

# Assuming the current working directory is the 'tests' directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import app
from fastapi.testclient import TestClient
from main import cbioportalRouter  

client = TestClient(cbioportalRouter)

def test_get_health_status():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_fetch_clinical_data():
    study_id = "acc_tcga"
    clinical_data_type = "SAMPLE"
    projection = "SUMMARY"
    request_data = {
        "ids": ["sample_id_1", "sample_id_2"],
        "attributeIds": ["attribute_id_1", "attribute_id_2"]
    }

    response = client.post(
        f"/studies/{study_id}/clinical-data/fetch",
        params={"clinicalDataType": clinical_data_type, "projection": projection},
        json=request_data,
    )

    assert response.status_code == 200
    # Add more specific assertions based on the expected response structure

# Run the tests
if __name__ == "__main__":
    import pytest
    pytest.main(["-v"])
