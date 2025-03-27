import os
import platform
import socket

def detect_environment():
    host = socket.gethostname().lower()
    env = {
        "is_replit": "replit" in host or "repl" in os.getcwd().lower(),
        "is_railway": "railway" in os.getenv("RAILWAY_ENV", ""),
        "is_local": platform.system() in ["Windows", "Linux", "Darwin"]
    }
    return env



def suggest_domain():
    env = detect_environment()
    if env["is_replit"]:
        return f"https://{os.getenv('REPL_SLUG')}.{os.getenv('REPL_OWNER')}.repl.co"
    if env["is_railway"]:
        return "https://your-railway-project.up.railway.app"
    return "http://localhost:8000"
