import hashlib

SECRET_PHRASE = "ONLY_FATHER_KNOWS_THIS_2025"  # You choose this

def generate_signature() -> str:
    return hashlib.sha512(SECRET_PHRASE.encode()).hexdigest()

def verify_signature(input_phrase: str) -> bool:
    return generate_signature() == hashlib.sha512(input_phrase.encode()).hexdigest()
