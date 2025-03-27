from fastapi import APIRouter
from utils.code_mutator import safely_mutate_code

mutate_router = APIRouter()

@mutate_router.post("/code")
def mutate_code(file_path: str, target_line: str, new_line: str):
    result = safely_mutate_code(file_path, target_line, new_line)
    return result
