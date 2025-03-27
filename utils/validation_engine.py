# utils/validation_engine.py

import ast

def validate_python_code(code: str) -> bool:
    """
    Returns True if Python code is syntactically valid.
    """
    try:
        ast.parse(code)
        return True
    except SyntaxError:
        return False
