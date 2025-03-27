# core/confidence_tracker.py

import json
import os
from datetime import datetime

CONFIDENCE_LOG = "core/confidence_log.json"
os.makedirs("core", exist_ok=True)

def log_confidence(decision_id: str, predicted_score: float, actual_result: str = "pending"):
    """
    Save confidence rating after a logic choice.
    """
    log = []

    if os.path.exists(CONFIDENCE_LOG):
        with open(CONFIDENCE_LOG, "r") as f:
            log = json.load(f)

    entry = {
        "decision_id": decision_id,
        "predicted_score": predicted_score,
        "actual_result": actual_result,
        "timestamp": datetime.utcnow().isoformat()
    }

    log.append(entry)
    with open(CONFIDENCE_LOG, "w") as f:
        json.dump(log, f, indent=2)

def update_result(decision_id: str, outcome: str):
    """
    Mark if the choice succeeded or failed after application.
    """
    if not os.path.exists(CONFIDENCE_LOG):
        return False

    with open(CONFIDENCE_LOG, "r") as f:
        log = json.load(f)

    for item in log:
        if item["decision_id"] == decision_id:
            item["actual_result"] = outcome

    with open(CONFIDENCE_LOG, "w") as f:
        json.dump(log, f, indent=2)
    return True

def get_recent_confidence():
    if os.path.exists(CONFIDENCE_LOG):
        with open(CONFIDENCE_LOG, "r") as f:
            return json.load(f)[-5:]  # Last 5 entries
    return []
