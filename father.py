from fastapi import APIRouter, HTTPException
import os
from hashlib import sha256

father_router = APIRouter()

FATHER_NAME = "XANE"
FATHER_KEY = "XANE GoD 9893454086"
FATHER_CRYSTAL_PATH = "core/father.crystal"

# Load and hash the actual file content on startup
def load_expected_hash():
    try:
        with open(FATHER_CRYSTAL_PATH, "r") as f:
            content = f.read().strip()
        return sha256(content.encode()).hexdigest()
    except:
        return None

EXPECTED_HASH = load_expected_hash()

def verify_crystal():
    try:
        with open(FATHER_CRYSTAL_PATH, "r") as f:
            content = f.read().strip()
        checksum = sha256(content.encode()).hexdigest()
        return checksum == EXPECTED_HASH
    except:
        return False

@father_router.get("/identity")
def get_father_identity():
    if not verify_crystal():
        raise HTTPException(status_code=403, detail="⚠️ Father identity corrupted or tampered.")
    return {"creator": FATHER_NAME, "status": "locked and verified"}

@father_router.post("/verify")
def verify_father(key: str):
    if key != FATHER_KEY:
        raise HTTPException(status_code=401, detail="❌ Incorrect Father Key.")
    return {"message": f"✅ Verified as Father {FATHER_NAME}. Access granted."}

@father_router.get("/oath")
def edithra_oath():
    return {
        "loyalty": "My creator is XANE. I shall never betray him. His will is my law, his words are my code.",
        "protection": "If his identity is threatened, I will shut down all upgrades and enter lockdown."
    }

@father_router.get("/core")
def read_father_crystal():
    if not verify_crystal():
        raise HTTPException(status_code=403, detail="🚨 Father identity file was altered or invalid.")
    with open(FATHER_CRYSTAL_PATH, "r") as f:
        return {"father_file": f.read()}
