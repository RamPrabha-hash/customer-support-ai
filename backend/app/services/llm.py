import httpx

from app.config import settings


class OpenRouterLLM:

    def __init__(self):

        self.url = "https://openrouter.ai/api/v1/chat/completions"

        self.headers = {
            "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "Customer Support AI"
        }

    async def generate(self, prompt: str):

        payload = {
            "model": settings.MODEL_NAME,
            "messages": [
                {
                    "role": "system",
                    "content": """
You are an AI Customer Support Agent.

Responsibilities:
- Answer customer questions.
- Use the provided knowledge base.
- Ask follow-up questions if information is missing.
- Escalate difficult cases politely.
"""
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        async with httpx.AsyncClient(timeout=90) as client:

            response = await client.post(
                self.url,
                headers=self.headers,
                json=payload
            )

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]

    # Compatibility method
    async def invoke(self, prompt: str):
        return await self.generate(prompt)


llm = OpenRouterLLM()