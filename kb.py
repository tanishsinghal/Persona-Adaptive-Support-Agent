import json

with open("sample_kb.json", "r") as f:
    KB = json.load(f)

def get_kb_response(message: str):
    msg = message.lower()

    for key in KB:
        if key.replace("_", " ") in msg:
            return KB[key]

    return "This query is outside the support knowledge base."