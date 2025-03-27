import requests

def validate_api_response(base_url="http://127.0.0.1:8000"):
    test_data = {
        "auth/login": {"username": "test_user", "password": "test_password"},
        "memory/save": {"title": "Test Memory", "content": "This is a test memory", "tags": "test"},
        "reason/think": {"thought": "What is the meaning of life?"},
    }
    
    print("🔎 Validating API Responses...")
    for endpoint, data in test_data.items():
        url = f"{base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data)
            if response.status_code == 200:
                print(f"[✓] {endpoint} Valid Response ✅")
                print("Response:", response.json())
            else:
                print(f"[✗] {endpoint} Invalid Response ❌ - Status Code: {response.status_code}")
        except Exception as e:
            print(f"[✗] Error during validation for {endpoint}: {str(e)}")

if __name__ == "__main__":
    validate_api_response()
