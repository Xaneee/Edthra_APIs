import requests

def test_api_connection(url, endpoint):
    print(f"🔎 Testing API at {url}{endpoint}...")
    try:
        response = requests.get(f"{url}{endpoint}")
        print(f"[✓] Status Code: {response.status_code}")
        print(f"Response: {response.text[:300]}")  # Display only first 300 chars
    except Exception as e:
        print(f"[✗] Error connecting to API: {e}")

if __name__ == "__main__":
    base_url = input("Enter API Base URL (e.g., http://localhost:8000): ")
    endpoint = input("Enter API Endpoint (e.g., /healthcheck or /status): ")
    test_api_connection(base_url, endpoint)
