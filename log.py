from fastapi import APIRouter
from datetime import datetime
from database import get_db

log_router = APIRouter()

@log_router.post("/event")
def log_event(message: str, reason: str = "general"):
    conn = get_db()
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    c.execute("INSERT INTO logs (timestamp, message, reason) VALUES (?, ?, ?)", (timestamp, message, reason))
    conn.commit()
    return {"status": "logged", "timestamp": timestamp}
