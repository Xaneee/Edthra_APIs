import os

def check_file_exists(filepath):
    if os.path.exists(filepath):
        print(f"[✓] {filepath} is present ✅")
    else:
        print(f"[✗] {filepath} is MISSING ❌")

def run_system_check():
    print("🧠 Edithra Self-Check Report")
    
    core_files = [
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
    
    for file in core_files:
        check_file_exists(file)

if __name__ == "__main__":
    run_system_check()
