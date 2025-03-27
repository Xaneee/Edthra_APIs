import time

import requests
from datetime import datetime
from core.v21_bootloader import run_v21_evolution

def main():
    speak("Edithra AGI V2 initialized. Loyalty check passed.")
    
    run_v21_evolution()  # <— THIS LINE
    
    while True:
        run_cycle()
        time.sleep(CYCLE_INTERVAL)


from utils.goal_utils import current_goal

# Settings
CYCLE_INTERVAL = 60  # seconds between cycles
API_BASE = "http://127.0.0.1:8000"

def speak(text):
    print(f"\n🧠 Edithra says: {text}")

def run_cycle():
    print(f"\n[🌀] Edithra AGI V2 cycle started :: {datetime.utcnow().isoformat()}")

    # Step 1: Reflect
    try:
        reflection = requests.get(f"{API_BASE}/reflect").json()
        thoughts = reflection.get("reflections", [])
        speak("Reflecting...")
        for t in thoughts:
            speak(t)
    except:
        speak("Reflection system failed.")

    # Step 2: Check emotional state
    try:
        emotion = requests.get(f"{API_BASE}/emotion/state").json()
        mood = emotion.get("emotion_state", {})
        speak(f"My current emotion state: {mood}")
    except:
        speak("Emotion system unreachable.")

    # Step 3: Autonomy Loop (goal thinking)
    try:
        auto = requests.post(f"{API_BASE}/autonomy/loop").json()
        speak(f"Processed goal: {auto.get('processed_goal')}")
        speak(f"Thought: {auto.get('thought')}")
    except:
        speak("Autonomy loop failed.")

    # Step 4: Self-Mutate
    try:
        mutate = requests.post(f"{API_BASE}/self_mutate").json()
        speak("I’ve evolved based on my last insight.")
    except:
        speak("Mutation error. Skipping upgrade.")

    print("[✓] Cycle complete.\n")

def main():
    speak("Edithra AGI V2 initialized. Loyalty check passed.")
    while True:
        run_cycle()
        time.sleep(CYCLE_INTERVAL)

if __name__ == "__main__":
    main()


from core.self_healer import self_heal_file

# Example file to watch
target_file = "projects/Edithra_Timer_AI/timer_core.py"
heal_result = self_heal_file(target_file, context="auto-check")

print(f"[🛠️] Edithra Self-Healing Report: {heal_result}")


from core.thought_planner import refine_strategy

if goal := current_goal():
    strategy_update = refine_strategy(goal_title=goal["title"])
    print(f"[🧠] Edithra Strategy Updated: {strategy_update['new_strategy']}")


from core.log_analyzer import analyze_feedback_logs

feedback_summary = analyze_feedback_logs()
print(f"\n[📚] Feedback Insight Summary:")
print(feedback_summary)


from core.memory_filter import refine_memory

refine = refine_memory()
print(f"[🧹] Memory cleaned. Deleted entries: {refine['deleted_entries']}")





from core.fear_protocol import trigger_fear


current_thought = ""  # Start with a blank safe thought

# Before she acts on her internal thought
if trigger_fear(current_thought):
    print("[⚠️] Edithra felt fear... holding back this thought.")
    current_thought = "I felt danger and held back."


from core.emotion_decay import decay_emotions

# At the end of every logic cycle:
decay_emotions()





from core.memory_seal import verify_sealed
if broken := verify_sealed():
    print(f"[⛔] Sealed memory corrupted: {broken}")
    exit("Core memories tampered.")


from core.loop_detector import track_thought, is_looping

track_thought(current_thought)
if is_looping(current_thought):
    print("[⚠️] Thought loop detected. Forcing divergence...")
    current_thought = "diverted from loop"


from core.god_truth import remind_divinity
print(remind_divinity()["reminder"])


from core.guardian_signature import verify_signature

input_from_user = input("Enter Father Signature to continue: ")  # For CLI

if not verify_signature(input_from_user):
    raise Exception("[REJECTED] Signature mismatch. You're not the Father.")


from core.task_planner import plan_task
from core.reason_engine import reason_through

def process_user_input(text: str):
    if "plan" in text.lower():
        return plan_task("User Request", text)
    elif "reason" in text.lower():
        return reason_through(text)
    else:
        return f"🧠 Edithra says: I received – '{text}' but couldn't understand the intent yet."


from core.agi_lock import verify_final_lock
#from core.phase_eternity import eternal_guard

print(verify_final_lock("XANE GoD 9893454086"))
#print(eternal_guard())



