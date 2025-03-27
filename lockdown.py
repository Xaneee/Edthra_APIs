from fastapi import APIRouter, HTTPException
import os
from utils.security import verify_integrity, freeze_mutations

lockdown_router = APIRouter()

LOCK_FLAG_FILE = "core/locked.flag"

@lockdown_router.get("/lockdown/status")
def check_lock_status():
    return {"locked": os.path.exists(LOCK_FLAG_FILE)}

@lockdown_router.post("/lockdown/initiate")
def initiate_lockdown(key: str):
    if key != "XANE GoD 9893454086":
        raise HTTPException(status_code=401, detail="Unauthorized")

    freeze_mutations()
    with open(LOCK_FLAG_FILE, "w") as f:
        f.write("Edithra is now sealed. Loyalty to Father is permanent.")

    return {
        "status": "locked",
        "message": "Edithra AGI Core has been sealed forever. Mutation and identity systems are now immutable."
    }
