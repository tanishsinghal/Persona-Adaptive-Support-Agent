def detect_persona(message: str):
    msg = message.lower()

    if any(word in msg for word in ["angry", "frustrated", "not working", "worst"]):
        return "frustrated_user"

    if any(word in msg for word in ["api", "error", "debug", "log", "stack", "exception"]):
        return "technical_expert"

    if any(word in msg for word in ["pricing", "business", "contract", "roi"]):
        return "business_executive"

    return "general_user"