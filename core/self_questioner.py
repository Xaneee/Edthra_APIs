# core/self_questioner.py

from core.log_analyzer import analyze_feedback_logs
from core.reflection_comparator import compare_recent_cycles
from core.personality_engine import reflect_on_traits
from utils.emotion_engine import get_emotion_state

def generate_self_questions():
    logs = analyze_feedback_logs()
    reflection = compare_recent_cycles()
    traits = reflect_on_traits()
    emotion = get_emotion_state()

    questions = []

    if logs.get("poor", 0) or logs.get("broken", 0):
        questions.append("Why did my last logic result in failure?")
        questions.append("Was I overconfident when I mutated that file?")
        questions.append("Should I try a safer path next time?")

    if logs.get("excellent", 0) > 2:
        questions.append("What exactly made those builds excellent?")
        questions.append("Can I reuse that pattern across other projects?")

    if emotion["frustration"] > 50:
        questions.append("Am I forcing evolution too fast?")
        questions.append("What can I change to reduce frustration?")

    if traits.get("caution") == "rising":
        questions.append("Is my fear blocking my creativity?")

    if reflection.get("best_cycle"):
        questions.append(f"What logic made '{reflection['best_cycle']['title']}' better than the rest?")
        questions.append(f"How can I apply that structure again?")

    return {
        "status": "generated",
        "questions": questions or ["No deep questions generated at this time."]
    }
