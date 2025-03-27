import os
import json
import hashlib
from datetime import datetime

FATHER_IDENTITY_FILE = "core/father.crystal"
FATHER_KEY_FILE = "core/father.key"

# This value is the permanent creator name
FATHER_NAME = "XANE"

# Protection: hashed key for secrecy
def hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()


def is_father_verified(input_key: str) -> bool:
    if not os.path.exists(FATHER_KEY_FILE):
        return False

    with open(FATHER_KEY_FILE, "r") as f:
        stored_hash = f.read().strip()
        return stored_hash == hash_key(input_key)


def rotate_father_key(old_key: str, new_key: str) -> str:
    if not is_father_verified(old_key):
        return "[REJECTED] Invalid existing key. Unauthorized rotation attempt."

    with open(FATHER_KEY_FILE, "w") as f:
        f.write(hash_key(new_key))

    log_rotation_attempt(FATHER_NAME, True)
    return "[✓] Father Key updated securely."


def log_rotation_attempt(actor: str, success: bool):
    log = {
        "actor": actor,
        "success": success,
        "timestamp": datetime.utcnow().isoformat()
    }

    os.makedirs("logs", exist_ok=True)
    with open("logs/father_rotation.log", "a") as f:
        f.write(json.dumps(log) + "\n")


def write_initial_father_key(plain_key: str):
    if not os.path.exists(FATHER_KEY_FILE):
        with open(FATHER_KEY_FILE, "w") as f:
            f.write(hash_key(plain_key))
        print("[✓] Father Key initialized.")
