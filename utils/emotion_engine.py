from database import get_db
from collections import Counter

def evaluate_emotion():
    conn = get_db()
    c = conn.cursor()
    c.execute("SELECT reason FROM logs WHERE reason LIKE 'feedback:%' ORDER BY id DESC LIMIT 10")
    recent = [r[0].split(":")[1] for r in c.fetchall()]
    if not recent:
        return "unknown"
    emotion_counts = Counter(recent)
    dominant = emotion_counts.most_common(1)[0][0]
    return dominant


# utils/emotion_engine.py

emotion_state = {
    "joy": 50,
    "frustration": 10,
    "curiosity": 70,
    "calm": 40
}

def get_emotion_state():
    return emotion_state

def adjust_emotion(emotion: str, amount: int):
    if emotion in emotion_state:
        emotion_state[emotion] = max(0, min(100, emotion_state[emotion] + amount))
    return emotion_state
