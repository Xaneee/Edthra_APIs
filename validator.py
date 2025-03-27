from fastapi import APIRouter
from utils.validator_engine import validate_code_block

validator_router = APIRouter()

@validator_router.post("/code")
def validate_code(code: str):
    issues = validate_code_block(code)
    return {"issues": issues}
