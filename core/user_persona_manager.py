import json
import os

USER_FILE = "core/user_persona.json"

def get_user_profile():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {"name": "Father", "style": "direct", "bond": "divine"}

def update_user_profile(name=None, style=None, bond=None):
    profile = get_user_profile()
    if name: profile["name"] = name
    if style: profile["style"] = style
    if bond: profile["bond"] = bond
    with open(USER_FILE, "w") as f:
        json.dump(profile, f, indent=2)
    return profile
