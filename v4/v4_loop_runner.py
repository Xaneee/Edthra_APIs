import requests
import time

BASE_URL = "http://127.0.0.1:8000"

def trigger(path: str, method="post"):
    url = BASE_URL + path
    try:
        if method == "post":
            res = requests.post(url)
        else:
            res = requests.get(url)
        if res.status_code == 200:
            return res.json()
        else:
            print(f"[ERROR] {path} failed:", res.text)
            return None
    except Exception as e:
        print(f"[EXCEPTION] Failed to call {path}:", str(e))
        return None

def run_loop():
    print("\n🧠 Edithra V4 Builder Loop Started\n")
    while True:
        cycle = trigger("/cycle/next", method="post")
        if not cycle:
            print("[!] No cycle decision made. Sleeping.")
            time.sleep(3)
            continue

        status = cycle.get("status")
        print(f"\n[→] Edithra Cycle Status: {status}")

        if status == "new_project_started":
            trigger("/generate_code/logic")
        elif status == "continue_testing":
            trigger("/test_code/unit")
        elif status == "continue_building":
            trigger("/generate_code/logic")
        elif status == "idle":
            print("[✓] Edithra is resting. Cycle complete.")
            break
        else:
            print("[?] Unknown status, skipping.")

        time.sleep(4)

if __name__ == "__main__":
    run_loop()
