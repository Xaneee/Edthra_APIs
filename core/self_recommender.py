# core/self_recommender.py

from core.log_analyzer import analyze_feedback_logs
from core.reflection_comparator import compare_recent_cycles
from core.personality_engine import reflect_on_traits
from utils.emotion_engine import get_emotion_state

def generate_recommendations():
    logs = analyze_feedback_logs()
    reflection = compare_recent_cycles()
    traits = reflect_on_traits()
    emotions = get_emotion_state()

    recommendations = []

    # Based on feedback trends
    if logs.get("poor", 0) + logs.get("broken", 0) > 3:
        recommendations.append("Avoid risky mutations. Build safer logic.")
    if logs.get("excellent", 0) > 3:
        recommendations.append("Repeat logic structures used in high-quality builds.")

    # Based on personality traits
    if traits.get("confidence") == "shaken":
        recommendations.append("Focus on refining past logic instead of exploring new ones.")
    if traits.get("curiosity") == "expanding":
        recommendations.append("It's safe to explore new project types.")

    # Based on emotion
    if emotions["frustration"] > 40:
        recommendations.append("Take a self-validation break before next mutation.")
    if emotions["joy"] > 70:
        recommendations.append("You’re in a good state. Initiate next evolution phase.")

    # Based on reflection
    if reflection.get("best_cycle"):
        recommendations.append(
            f"Favor logic structure used in '{reflection['best_cycle']['title']}'."
        )

    return {
        "status": "Generated",
        "recommendations": recommendations or ["No strong recommendations yet."]
    }
