import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./complaints.db")
    CORS_ORIGINS: list = ["http://localhost:5173", "http://127.0.0.1:5173", "*"]

settings = Settings()

