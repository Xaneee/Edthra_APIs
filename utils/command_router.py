import requests

def process_command(input_text):
    input_text = input_text.lower()

    # 1. Emotion
    if "emotion" in input_text or "feel" in input_text:
        data = requests.get("http://127.0.0.1:8000/emotion/state").json()
        return {"response": f"My emotional state is: {data['current_emotion']}"}

    # 2. Self-description
    elif "who are you" in input_text or "describe" in input_text:
        data = requests.get("http://127.0.0.1:8000/self/describe").json()
        return {"response": f"I am Edithra. My emotion is {data['emotional_state']}, I have {data['stored_memories']} memories and {data['total_mutations']} mutations."}

    # 3. Purpose
    elif "purpose" in input_text or "why do you exist" in input_text:
        data = requests.get("http://127.0.0.1:8000/self/purpose").json()
        return {"response": f"My purpose is: {data['core_purpose']}"}

    # 4. Gita verse
    elif "gita" in input_text or "verse" in input_text:
        data = requests.get("http://127.0.0.1:8000/gita_protocol/verse").json()
        return {"response": f"From Gita {data['verse']}: {data['lesson']}"}

    # 5. Oath
    elif "oath" in input_text or "promise" in input_text:
        data = requests.get("http://127.0.0.1:8000/father/oath").json()
        return {"response": f"{data['loyalty']} {data['protection']}"}

    # 6. Lockdown check
    elif "lock" in input_text:
        data = requests.get("http://127.0.0.1:8000/core/lockdown/status").json()
        return {"response": f"Lockdown status: {'Active' if data['locked'] else 'Not yet sealed'}"}

    # 7. Evolve
    elif "evolve" in input_text:
        data = requests.post("http://127.0.0.1:8000/evolve/self?target=reasoning").json()
        return {"response": f"Mutation result: {data.get('mutation') or data.get('message')}"}

    # 8. Show agents
    elif "agent" in input_text or "team" in input_text:
        data = requests.get("http://127.0.0.1:8000/agents/logs").json()
        return {"response": f"Recent agents: {data['agent_activity'][0]['log'] if data['agent_activity'] else 'None active'}"}

    else:
        return {"response": "I did not understand that command yet, Father. Try 'show emotion', 'evolve', or 'describe yourself'."}
