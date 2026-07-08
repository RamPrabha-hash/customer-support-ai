import random
from datetime import datetime

ESCALATION_KEYWORDS = [
    "refund not received",
    "refund delayed",
    "legal",
    "court",
    "complaint",
    "manager",
    "damaged product",
    "wrong product",
    "angry",
    "cancel order",
    "not delivered",
    "replacement",
    "broken",
    "defective",
    "escalate",
    "human"
]


def needs_escalation(message: str):

    message = message.lower()

    for keyword in ESCALATION_KEYWORDS:
        if keyword in message:
            return True

    return False


def create_ticket(message: str):

    ticket_id = f"TKT-{random.randint(1000,9999)}"

    return f"""
🚨 Human Assistance Required

Ticket ID : {ticket_id}

Priority : HIGH

Created : {datetime.now().strftime("%d-%m-%Y %H:%M")}

Issue Summary:
{message}

Our customer support team will contact you shortly.
"""