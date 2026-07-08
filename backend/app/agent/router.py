def detect_intent(message: str):

    msg = message.lower()

    if any(word in msg for word in [
        "return",
        "refund",
        "shipping",
        "delivery",
        "warranty",
        "payment"
    ]):
        return "rag"

    elif any(word in msg for word in [
        "problem",
        "issue",
        "error",
        "not working",
        "failed",
        "unable"
    ]):
        return "support"

    elif any(word in msg for word in [
        "manager",
        "complaint",
        "angry",
        "lawyer",
        "court",
        "human",
        "damaged",
        "broken"
    ]):
        return "escalation"

    return "general"