class ConversationMemory:

    def __init__(self):
        self.history = []

    def add_message(self, role: str, message: str):
        self.history.append(
            {
                "role": role,
                "content": message
            }
        )

    def get_history(self):

        if len(self.history) == 0:
            return ""

        chat = ""

        for item in self.history:
            chat += f"{item['role']}: {item['content']}\n"

        return chat

    def clear(self):
        self.history = []


memory = ConversationMemory()