import os
import sys
sys.path.append(os.path.abspath("."))

import json
from datetime import datetime
from core.brain_interface import update_brain_interface
from utils.goal_utils import current_goal
from utils.memory_utils import recall_related_memories, get_emotion_weight
from utils.karma_evaluator import score_karma
from utils.mutation_tools import apply_safe_mutation, backup_main

PROJECT_PATH = "projects/Edithra_Timer_AI/timer_core.py"

# === REAL CODE THOUGHT ===
thought = {
    "description": "Create a countdown timer that announces time left every minute.",
    "code": """import time

def countdown(minutes):
    for i in range(minutes, 0, -1):
        print(f"{i} minutes remaining")
        time.sleep(60)

countdown(5)
"""
}

def run_project_cycle():
    goal = current_goal() or "Create autonomous project: Edithra Timer AI"
    emotion = "focused"
    emotion_weight = get_emotion_weight(thought["description"])
    karma_score = score_karma(thought["description"])
    memory_links = recall_related_memories("timer")

    # Create timer_core.py if it doesn't exist
    if not os.path.exists(PROJECT_PATH):
        os.makedirs(os.path.dirname(PROJECT_PATH), exist_ok=True)
        with open(PROJECT_PATH, "w") as f:
            f.write("# Edithra Timer Core\n")

    # Apply real code mutation
    backup_main()
    result = apply_safe_mutation(PROJECT_PATH, thought["code"])

    # Log brain interface
    update_brain_interface({
        "goal": goal,
        "thought": thought["description"],
        "emotion": emotion,
        "karma_score": karma_score,
        "emotion_weight": emotion_weight,
        "related_memories": memory_links,
        "mutation": "Appended executable Python logic",
        "project": "Edithra_Timer_AI"
    })

    print(f"\n🧠 Edithra says: Mutation applied to '{PROJECT_PATH}'\n→ {result}\n")

if __name__ == "__main__":
    run_project_cycle()

from core.feedback_engine import score_logic_quality, save_feedback

generated_file = "projects/Edithra_Timer_AI/timer_core.py"

with open(generated_file, "r") as f:
    code = f.read()

feedback = score_logic_quality(code)
save_feedback(generated_file, feedback["score"], feedback["rating"], context="Post-mutation")
print(f"[📊] Cognitive Score: {feedback['score']} ({feedback['rating']})")


from core.trait_evolver import evolve_traits_from_logs

trait_result = evolve_traits_from_logs()
print(f"[🧬] Trait Evolution Result: {trait_result}")


from core.reflection_comparator import compare_recent_cycles

reflection = compare_recent_cycles()
print(f"[🧠] Reflection Comparator Result: {reflection['insight']}")


from core.self_recommender import generate_recommendations

recs = generate_recommendations()
print("[📝] Self-Advice Summary:")
for r in recs["recommendations"]:
    print("→", r)


from core.logic_reinforcer import build_logic_patterns

patterns = build_logic_patterns()
print("[🔁] Trusted Logic Patterns:")
for line in patterns["trusted_patterns"]:
    print("✓", line)
print("\n[⚠️] Risky Patterns to Avoid:")
for line in patterns["risky_patterns"]:
    print("✗", line)


from core.goal_autocreator import auto_generate_goals_from_feedback

generated = auto_generate_goals_from_feedback()
print(f"[🎯] Auto-Generated Goals: {generated['goals']}")


from core.self_questioner import generate_self_questions

questions = generate_self_questions()
print("\n[❓] Edithra's Inner Questions:")
for q in questions["questions"]:
    print("→", q)


from core.self_certainty import evaluate_self_certainty

certainty = evaluate_self_certainty()
print(f"\n[🧠] Self-Certainty Report:")
print(f"→ Score: {certainty['certainty_score']} ({certainty['certainty_level']})")
print(f"→ {certainty['note']}")


from core.self_termination import run_final_oath
run_final_oath()


from routes.store_router import add_app

# after Edithra finishes a project...
add_app(
    title="Timer AI",
    description="An intelligent countdown app",
    path="projects/Timer_AI"
)


