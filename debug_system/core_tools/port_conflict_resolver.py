import psutil

def find_conflicting_ports(target_ports=[8000, 8080, 5000]):
    print("🔎 Checking for Port Conflicts...")
    conflicting_ports = []

    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port in target_ports:
            conflicting_ports.append(conn.laddr.port)

    if conflicting_ports:
        print(f"[⚠️] Conflict detected on ports: {conflicting_ports}")
    else:
        print("[✓] No Port Conflicts Found ✅")

if __name__ == "__main__":
    find_conflicting_ports()
