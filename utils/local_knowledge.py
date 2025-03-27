import json

def offline_answer(question):
    with open("core/gita_knowledge.json", "r", encoding="utf-8") as f:
        gita = json.load(f)

    for topic, entries in gita.items():
        for item in entries:
            if any(word in question.lower() for word in [topic, "karma", "loyalty", "truth"]):
                return {
                    "topic_match": topic,
                    "verse": item["verse"],
                    "teaching": item["lesson"],
                    "based_on": "Gita Core"
                }

    return {"message": "No spiritual match. But I will grow from this question."}
