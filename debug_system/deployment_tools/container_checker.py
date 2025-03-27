import subprocess

def list_containers():
    print("📦 Listing Docker Containers...")
    try:
        result = subprocess.run(["docker", "ps", "-a"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"[✗] Failed to list containers: {e}")

if __name__ == "__main__":
    list_containers()
