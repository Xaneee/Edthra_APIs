import os
import re

LOG_FOLDER = "logs"
ERROR_PATTERN = re.compile(r"\[ERROR\].*")

def analyze_logs():
    print("🔎 Analyzing Logs for Errors...")
    if not os.path.exists(LOG_FOLDER):
        print("[✗] Logs folder not found.")
        return
    
    error_count = 0
    for filename in os.listdir(LOG_FOLDER):
        file_path = os.path.join(LOG_FOLDER, filename)
        if os.path.isfile(file_path) and filename.endswith(".log"):
            with open(file_path, "r", encoding="utf-8") as log_file:
                lines = log_file.readlines()
                for line in lines:
                    if ERROR_PATTERN.search(line):
                        print(f"[❗] Error found in {filename}: {line.strip()}")
                        error_count += 1

    if error_count == 0:
        print("[✓] No Errors Detected ✅")
    else:
        print(f"[⚠️] {error_count} Errors Found")

if __name__ == "__main__":
    analyze_logs()
