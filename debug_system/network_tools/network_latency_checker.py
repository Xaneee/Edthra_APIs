import time
import requests

def check_latency(url):
    print(f"⏳ Checking latency for {url}...")
    try:
        start = time.time()
        response = requests.get(url)
        end = time.time()
        latency = (end - start) * 1000
        print(f"[✓] Response Time: {latency:.2f} ms | Status: {response.status_code}")
    except Exception as e:
        print(f"[✗] Failed to reach {url}. Error: {e}")

if __name__ == "__main__":
    url = input("Enter URL to check latency (e.g., http://localhost:8000): ")
    check_latency(url)
