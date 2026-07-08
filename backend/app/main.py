from fastapi import FastAPI

from app.config import settings
from app.routes.chat import router as chat_router

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Agentic AI Customer Support Backend"
)

app.include_router(chat_router)


@app.get("/")
async def home():
    return {
        "message": "Customer Support AI Backend Running 🚀"
    }


@app.get("/health")
async def health():
    return {
        "status": "Healthy",
        "model": settings.MODEL_NAME,
        "api_key_loaded": settings.OPENROUTER_API_KEY is not None
    }