import os

def check_deployment_logs(log_path="logs/deployment.log"):
    print(f"📜 Checking Deployment Logs: {log_path}")
    if not os.path.exists(log_path):
        print("[✗] Log file not found.")
        return

    try:
        with open(log_path, "r", encoding="utf-8") as f:
            logs = f.readlines()
            if logs:
                print("[✓] Recent Logs:")
                print("".join(logs[-10:]))  # Display last 10 lines
            else:
                print("[⚠️] No logs found.")
    except Exception as e:
        print(f"[✗] Error reading log file: {e}")

if __name__ == "__main__":
    check_deployment_logs()
