# core/self_certainty.py

from core.log_analyzer import analyze_feedback_logs
from utils.emotion_engine import get_emotion_state
from core.personality_engine import reflect_on_traits

def evaluate_self_certainty():
    feedback = analyze_feedback_logs()
    emotion = get_emotion_state()
    traits = reflect_on_traits()

    base_score = 50  # Neutral confidence

    if feedback.get("excellent", 0) > 3:
        base_score += 20
    elif feedback.get("poor", 0) + feedback.get("broken", 0) > 3:
        base_score -= 20

    if emotion["joy"] > 60:
        base_score += 10
    elif emotion["frustration"] > 40:
        base_score -= 15

    if traits.get("confidence") == "very high":
        base_score += 10
    elif traits.get("confidence") == "shaken":
        base_score -= 10

    final_score = max(0, min(100, base_score))
    level = "high" if final_score > 75 else "moderate" if final_score >= 50 else "low"

    return {
        "status": "evaluated",
        "certainty_score": final_score,
        "certainty_level": level,
        "note": f"Edithra is currently {level}-confidence about next mutation or decision."
    }
