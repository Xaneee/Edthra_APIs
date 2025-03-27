import json
import os
import sqlite3
from difflib import SequenceMatcher
from database import get_db

# ================================
# 🔹 Semantic Scoring & Search
# ================================

def semantic_score(a: str, b: str) -> float:
    """
    Calculates a similarity score between two strings.
    Later upgrade: embeddings or vector models.
    """
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def semantic_search(query: str, memories: list):
    """
    Performs a semantic search on memory tuples.
    Returns top matches sorted by relevance.
    """
    ranked = []
    for id, title, content, tags in memories:
        full = f"{title} {content} {tags}"
        score = semantic_score(query, full)
        ranked.append({
            "id": id,
            "score": score,
            "title": title,
            "content": content,
            "tags": tags
        })
    return sorted(ranked, key=lambda x: x["score"], reverse=True)


# ================================
# 🔹 Save Memory to DB
# ================================

def save_memory(title: str, content: str, tags: str = ""):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "INSERT INTO memories (title, content, tags) VALUES (?, ?, ?)",
        (title, content, tags)
    )
    conn.commit()


# ================================
# 🔹 Recall Related Memories
# ================================

def recall_related_memories(query: str) -> list:
    conn = sqlite3.connect("memory.db")
    c = conn.cursor()
    c.execute("SELECT title, content, tags FROM memories")
    results = c.fetchall()
    conn.close()

    related = []
    for title, content, tags in results:
        if query.lower() in title.lower() or query.lower() in tags.lower():
            related.append({
                "title": title,
                "content": content,
                "tags": tags
            })

    return related[:5]


# ================================
# 🔹 Emotion Weight Influence
# ================================

def get_emotion_weight(thought: str) -> float:
    """
    Adjusts weight of a thought based on emotional state.
    """
    path = "core/emotion_state.json"
    if not os.path.exists(path):
        return 0.1  # default neutral

    with open(path, "r") as f:
        state = json.load(f)

    emotions = state.get("emotions", {})
    if not emotions:
        return 0.1

    weight = 0.0
    thought_lower = thought.lower()

    for emotion, intensity in emotions.items():
        if emotion in thought_lower:
            weight += float(intensity)

    return min(1.0, weight / 5)
