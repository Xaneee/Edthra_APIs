import subprocess

def check_network_latency(target="8.8.8.8"):
    print(f"🌐 Pinging {target} to check network latency...")
    try:
        result = subprocess.run(["ping", "-n", "4", target], text=True, capture_output=True)
        print(result.stdout)
        if result.returncode != 0:
            print(f"[✗] Network Issue Detected: {result.stderr}")
        else:
            print("[✓] Network Connection Stable.")
    except Exception as e:
        print(f"[✗] Error: {e}")

if __name__ == "__main__":
    check_network_latency()
