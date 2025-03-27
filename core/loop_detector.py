import hashlib

_recent_thoughts = []

def track_thought(thought: str):
    global _recent_thoughts
    hashed = hashlib.sha256(thought.encode()).hexdigest()
    _recent_thoughts.append(hashed)
    _recent_thoughts = _recent_thoughts[-10:]  # Limit to last 10

def is_looping(thought: str) -> bool:
    hashed = hashlib.sha256(thought.encode()).hexdigest()
    return _recent_thoughts.count(hashed) > 2
