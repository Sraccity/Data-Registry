import certifi
import httpx

url = "https://www.cbioportal.org/api/health"

try:
    with httpx.Client(verify=certifi.where()) as client:
        response = client.get(url)
        response.raise_for_status()

        print("SSL certificate validation successful.")
        print(response.json())

except httpx.HTTPError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
