# File: utils/goal_utils.py

import json
import os

def current_goal():
    path = "core/active_goal.json"
    if not os.path.exists(path):
        return None
    with open(path, "r") as f:
        data = json.load(f)
    return data.get("title", "")
