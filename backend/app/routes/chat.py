from fastapi import APIRouter, HTTPException

from app.schemas import ChatRequest, ChatResponse
from app.services.llm import llm
from app.services.rag import retrieve
from app.services.memory import memory
from app.services.escalation import (
    needs_escalation,
    create_ticket
)
from app.agent.router import detect_intent

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    try:

        # Save customer message
        memory.add_message("Customer", request.message)

        # Detect intent
        intent = detect_intent(request.message)

        # Escalation Agent
        if intent == "escalation" or needs_escalation(request.message):

            ticket = create_ticket(request.message)

            memory.add_message("Assistant", ticket)

            return ChatResponse(
                response=ticket
            )

        # Memory
        history = memory.get_history()

        # RAG
        knowledge = retrieve(request.message)

        prompt = f"""
You are an intelligent AI Customer Support Agent.

Conversation History:
{history}

Knowledge Base:
{knowledge}

Detected Intent:
{intent}

Customer Question:
{request.message}

Instructions:

If intent == rag:
Answer using the knowledge base.

If intent == support:
Guide the customer step-by-step.

If intent == general:
Answer politely.

Always remember previous conversation.

If information is missing,
ask follow-up questions.
"""

        answer = await llm.generate(prompt)

        memory.add_message(
            "Assistant",
            answer
        )

        return ChatResponse(
            response=answer
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )