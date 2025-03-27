import socket

def check_ports(ports):
    print("🔎 Checking Port Availability...")
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            result = s.connect_ex(('localhost', port))
            if result == 0:
                print(f"[⚠️] Port {port} is in use.")
            else:
                print(f"[✓] Port {port} is available.")

if __name__ == "__main__":
    ports_to_check = input("Enter ports separated by commas (e.g., 8000, 8080, 5000): ")
    ports = [int(p.strip()) for p in ports_to_check.split(",")]
    check_ports(ports)
