
def should_escalate(persona, message, turn_count):
    msg = message.lower()

    if "human" in msg or "agent" in msg:
        return True

    if persona == "frustrated_user" and turn_count >= 2:
        return True

    if persona == "business_executive":
        return True

    return False