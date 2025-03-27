import os
import time

LOG_FOLDER = "logs"

def monitor_logs(interval=2):
    print("🕵️ Monitoring Logs for Real-Time Updates...")
    if not os.path.exists(LOG_FOLDER):
        print("[✗] Logs folder not found.")
        return

    file_track = {}
    try:
        while True:
            for filename in os.listdir(LOG_FOLDER):
                file_path = os.path.join(LOG_FOLDER, filename)
                if os.path.isfile(file_path) and filename.endswith(".log"):
                    current_size = os.path.getsize(file_path)
                    
                    # Track new or updated logs
                    if filename not in file_track:
                        file_track[filename] = current_size
                        print(f"[📖] Tracking new log file: {filename}")
                    elif file_track[filename] < current_size:
                        file_track[filename] = current_size
                        print(f"[⚡] Log Updated: {filename}")
                        with open(file_path, "r", encoding="utf-8") as log_file:
                            log_file.seek(file_track[filename] - 500 if current_size > 500 else 0)
                            print(log_file.read())
            time.sleep(interval)
    except KeyboardInterrupt:
        print("[✓] Log Monitoring Stopped")

if __name__ == "__main__":
    monitor_logs()
