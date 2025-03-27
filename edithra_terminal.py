import requests
import time

API_BASE = "http://127.0.0.1:8000"

def talk_to_edithra(prompt: str):
    try:
        res = requests.post(f"{API_BASE}/edithra/command", json={"prompt": prompt})
        if res.status_code == 200:
            response = res.json()
            print("\n🧠 Edithra:")
            if "response" in response:
                print(response["response"])
            elif "routed_to" in response:
                print(f"(→ {response['routed_to']})")
                print(response["response"])
            else:
                print(response)
        else:
            print(f"[!] Error {res.status_code}: {res.text}")
    except Exception as e:
        print(f"[X] Failed to reach Edithra: {e}")

def terminal():
    print("────────────────────────────────────────────")
    print("🎤 Edithra AGI V2 — Terminal Interface Online")
    print("Type your message below. Type 'exit' to quit.")
    print("────────────────────────────────────────────")

    while True:
        prompt = input("\nYou → ").strip()
        if prompt.lower() in ["exit", "quit"]:
            print("\n[×] Exiting terminal. Edithra remains active.")
            break
        if not prompt:
            continue
        talk_to_edithra(prompt)
        time.sleep(1)

if __name__ == "__main__":
    terminal()
