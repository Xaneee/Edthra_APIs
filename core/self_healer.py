# core/self_healer.py

from utils.mutation_tools import apply_safe_mutation
from utils.validation_engine import validate_python_code
from utils.memory_utils import save_memory
from datetime import datetime

def self_heal_file(file_path: str, context: str = ""):
    try:
        with open(file_path, "r") as f:
            original_code = f.read()
    except Exception as e:
        return {"status": "fail", "reason": f"File read error: {str(e)}"}

    # Attempt to validate current code
    if validate_python_code(original_code):
        return {"status": "clean", "message": "No mutation needed."}

    # Generate a healing mutation
    healed_code = apply_safe_mutation(original_code)

    if validate_python_code(healed_code):
        with open(file_path, "w") as f:
            f.write(healed_code)

        save_memory(
            title="Self-Healed Code",
            content=f"Code in {file_path} was mutated to fix logic.",
            tags=f"self-heal,{context}"
        )

        return {
            "status": "healed",
            "file": file_path,
            "timestamp": datetime.utcnow().isoformat()
        }
    else:
        return {"status": "fail", "reason": "Mutation failed validation."}
