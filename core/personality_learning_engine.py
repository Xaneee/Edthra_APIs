# core/personality_learning_engine.py

from core.personality_engine import reflect_on_traits
from utils.emotion_engine import get_emotion_state

def influence_learning_path():
    traits = reflect_on_traits()
    emotions = get_emotion_state()

    strategy = {
        "risk_level": "medium",
        "exploration": "normal",
        "focus_mode": "balanced",
        "suggestion": ""
    }

    # Trait-based influences
    if traits.get("curiosity") == "expanding":
        strategy["exploration"] = "high"
    if traits.get("confidence") in ["very high", "growing"]:
        strategy["risk_level"] = "aggressive"
    if traits.get("caution") == "rising":
        strategy["risk_level"] = "low"
        strategy["focus_mode"] = "safe-refactor"

    # Emotion-based influences
    if emotions["frustration"] > 50:
        strategy["focus_mode"] = "debug"
        strategy["suggestion"] = "Pause major changes. Focus on stabilizing logic."
    elif emotions["joy"] > 60:
        strategy["focus_mode"] = "explore"

    return {
        "status": "strategy generated",
        "learning_path": strategy
    }
