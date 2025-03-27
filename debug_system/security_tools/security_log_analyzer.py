import os
import re

LOG_FOLDER = "logs"
SECURITY_PATTERN = re.compile(r"\[SECURITY\].*")

def analyze_security_logs():
    print("🔍 Analyzing Security Logs...")
    if not os.path.exists(LOG_FOLDER):
        print("[✗] Logs folder not found.")
        return
    
    issues_found = 0
    for filename in os.listdir(LOG_FOLDER):
        file_path = os.path.join(LOG_FOLDER, filename)
        if os.path.isfile(file_path) and filename.endswith(".log"):
            with open(file_path, "r", encoding="utf-8") as log_file:
                lines = log_file.readlines()
                for line in lines:
                    if SECURITY_PATTERN.search(line):
                        print(f"[⚠️] Security Alert in {filename}: {line.strip()}")
                        issues_found += 1

    if issues_found == 0:
        print("[✓] No Security Alerts Found.")
    else:
        print(f"[🚨] Total Security Alerts: {issues_found}")

if __name__ == "__main__":
    analyze_security_logs()
