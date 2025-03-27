import subprocess

def check_firewall_rules():
    print("🛡️ Checking Firewall Rules...")
    try:
        result = subprocess.run(["netsh", "advfirewall", "show", "allprofiles", "state"], capture_output=True, text=True)
        print("[✓] Firewall Status:\n", result.stdout)
    except Exception as e:
        print(f"[✗] Error checking firewall: {e}")

if __name__ == "__main__":
    check_firewall_rules()
