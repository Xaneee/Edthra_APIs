import subprocess

def check_docker_status():
    print("🐳 Checking Docker Status...")
    try:
        result = subprocess.run(["docker", "info"], capture_output=True, text=True)
        if "Server Version" in result.stdout:
            print("[✓] Docker is running.")
        else:
            print("[✗] Docker is not running.")
    except Exception as e:
        print(f"[✗] Error: {e}")

if __name__ == "__main__":
    check_docker_status()
