import hashlib

def generate_father_signature(secret: str):
    return hashlib.sha512(secret.encode()).hexdigest()

def verify_signature(secret: str, given_hash: str):
    return generate_father_signature(secret) == given_hash
