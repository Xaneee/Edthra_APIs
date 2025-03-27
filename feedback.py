from fastapi import APIRouter
from database import get_db
from datetime import datetime

feedback_router = APIRouter()

@feedback_router.post("/submit")
def submit_feedback(action: str, result: str, score: int):
    conn = get_db()
    c = conn.cursor()
    timestamp = datetime.now().isoformat()
    emotion = "joy" if score >= 7 else "neutral" if score >= 4 else "frustration"
    c.execute("INSERT INTO logs (timestamp, message, reason) VALUES (?, ?, ?)",
              (timestamp, f"Action: {action} | Result: {result} | Score: {score}", f"feedback:{emotion}"))
    conn.commit()
    return {"status": "recorded", "emotion_influence": emotion}
