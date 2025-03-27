import os

files = [
    "core/phase_eternity.py",
    "core/memory_utils.py",
    "core/reason_engine.py",
    "core/self_mutate.py",
    "core/project_initializer.py",
    "core/store_db.json",
    "core/agi_lock.py",
    "core/empathy_engine.py",
    "core/monetization_planner.py",
    "core/web_crawler.py",
    "core/self_trainer.py",
    "core/ui_generator.py"
]

def run_system_check():
    print("🧠 Edithra Self-Check Report")
    for f in files:
        if os.path.exists(f):
            print(f"[✓] {f} is present ✅")
        else:
            print(f"[✗] {f} is MISSING ❌")

if __name__ == "__main__":
    run_system_check()
