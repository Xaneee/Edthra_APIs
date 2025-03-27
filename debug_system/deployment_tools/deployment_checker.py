import requests


def check_service_status(url):
    print(f"🌐 Checking Service Status at {url}...")
    try:
        response = requests.get(url)
        print(f"[✓] Status Code: {response.status_code}")
        print(f"Response: {response.text[:300]}")  # Print first 300 characters of response
    except requests.RequestException as e:
        print(f"[✗] Failed to connect to service: {e}")

if __name__ == "__main__":
    service_url = input("Enter the Service URL (e.g., http://localhost:8000): ")
    check_service_status(service_url)
