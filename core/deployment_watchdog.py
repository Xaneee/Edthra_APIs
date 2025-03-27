import datetime

LOG_PATH = "logs/deployment.log"

def log_event(event):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.datetime.utcnow().isoformat()}] {event}\n")

def read_logs():
    with open(LOG_PATH, "r") as f:
        return f.read()
