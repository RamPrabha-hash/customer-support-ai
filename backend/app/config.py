import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    APP_NAME = "Customer Support AI"

    APP_VERSION = "1.0"

    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

    MODEL_NAME = os.getenv(
        "MODEL_NAME",
        "nvidia/nemotron-3-ultra-550b-a55b:free"
    )


settings = Settings()