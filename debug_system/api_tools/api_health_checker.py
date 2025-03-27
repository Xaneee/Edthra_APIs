import requests

def check_api_health(base_url="http://127.0.0.1:8000"):
    endpoints = [
        "/auth/login",
        "/memory/save",
        "/memory/recall",
        "/log/event",
        "/reason/think",
        "/task/plan",
        "/mutate/code",
        "/search_knowledge/query",
        "/self_validate/code",
        "/agent_manager/spawn",
        "/gita_protocol/verse",
        "/father/identity"
    ]

    print("🔎 Checking API Health Status...")
    for endpoint in endpoints:
        url = f"{base_url}{endpoint}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[✓] {endpoint} is UP ✅")
            else:
                print(f"[✗] {endpoint} is DOWN ❌ - Status Code: {response.status_code}")
        except Exception as e:
            print(f"[✗] Error checking {endpoint}: {str(e)}")

if __name__ == "__main__":
    check_api_health()
