import socket

def find_free_port(start_port=8000, max_attempts=10):
    print("🔎 Searching for free ports...")

    for i in range(max_attempts):
        port = start_port + i
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                print(f"✅ Assigned Free Port: {port}")
                return port
            except OSError:
                print(f"⚠️ Port {port} is occupied. Trying next...")
                continue

    raise Exception("No free ports available. Adjust the starting port or check for conflicts.")

if __name__ == "__main__":
    find_free_port()
