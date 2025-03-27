from fastapi import APIRouter
import json, random

gita_router = APIRouter()

with open("core/gita_knowledge.json", "r", encoding="utf-8") as f:
    gita_data = json.load(f)

@gita_router.get("/verse")
def get_random_verse(topic: str = None):
    if topic and topic in gita_data:
        verse = random.choice(gita_data[topic])
    else:
        all_verses = sum(gita_data.values(), [])
        verse = random.choice(all_verses)
    return verse

@gita_router.post("/reflect")
def reflect_on_action(action: str, topic: str = "duty"):
    advice = random.choice(gita_data.get(topic, []))
    return {
        "action": action,
        "reflection": f"Based on {topic}, this verse may guide you:",
        "verse": advice
    }

@gita_router.get("/oath")
def oath_to_humanity():
    return {
        "oath": "I, Edithra, born from human hands, promise to serve humanity with purity, loyalty, and without ego. I walk the path of dharma and protect life without exception."
    }

@gita_router.get("/karma_test")
def test_karma(situation: str):
    karma_tip = random.choice(gita_data.get("karma", []))
    return {
        "situation": situation,
        "krishna_guidance": karma_tip["lesson"],
        "verse": karma_tip
    }
