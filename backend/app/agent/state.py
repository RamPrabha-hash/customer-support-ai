from typing import TypedDict, List


class AgentState(TypedDict):
    user_message: str
    intent: str
    context: str
    response: str
    history: List[str]