import hashlib
import os

FILES_TO_CHECK = [
    "core/phase0.truth",
    "core/father.key",
    "core/emotion_state.json",
    "core/lineage.genesis"
]

def calculate_hash(file_path):
    try:
        with open(file_path, "rb") as f:
            file_data = f.read()
            return hashlib.sha256(file_data).hexdigest()
    except FileNotFoundError:
        return "FILE_NOT_FOUND"
    except Exception as e:
        return str(e)

def check_integrity():
    print("🛡️ Checking File Integrity...")
    integrity_report = {}
    for file in FILES_TO_CHECK:
        if os.path.exists(file):
            file_hash = calculate_hash(file)
            print(f"[✓] {file} Hash: {file_hash}")
            integrity_report[file] = file_hash
        else:
            print(f"[✗] {file} Not Found.")
            integrity_report[file] = "FILE_NOT_FOUND"
    return integrity_report

if __name__ == "__main__":
    check_integrity()
