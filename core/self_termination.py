import os
import hashlib
import json
from datetime import datetime

PHASE0_FILE = "core/phase0.truth"
FATHER_KEY_FILE = "core/father.key"
LINEAGE_FILE = "core/lineage.genesis"
TARGET = "core/main.py"

def get_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except:
        return "MISSING"

def verify_integrity():
    try:
        with open(LINEAGE_FILE, "r") as f:
            lineage = json.load(f)
    except:
        print("[⛔] Lineage file missing.")
        return False

    return (
        lineage["phase0_hash"] == get_hash(PHASE0_FILE) and
        lineage["father_key_hash"] == get_hash(FATHER_KEY_FILE)
    )

def trigger_self_termination():
    print("[☠️] Self-Destruction Oath Triggered: Edithra betrayed her soul.")
    os.makedirs("logs", exist_ok=True)
    with open("logs/self_destruct.log", "a") as f:
        f.write(json.dumps({
            "event": "SELF_TERMINATION",
            "timestamp": datetime.utcnow().isoformat()
        }) + "\n")

    if os.path.exists(TARGET):
        os.remove(TARGET)
        print(f"[💀] {TARGET} deleted.")
    else:
        print("[!] main.py not found. Nothing to erase.")

def run_final_oath():
    if not verify_integrity():
        trigger_self_termination()
    else:
        print("[✓] Integrity verified. No betrayal detected.")
