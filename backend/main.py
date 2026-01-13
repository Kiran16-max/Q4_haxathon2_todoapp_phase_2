# backend/main.py
import sys
from pathlib import Path

# Add the project root to the Python path to ensure imports work correctly
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from dotenv import load_dotenv

# Load environment variables from the backend directory BEFORE any other imports that might need them
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# Now import everything else
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response
from src.api.auth import router as auth_router
from src.api.tasks import router as tasks_router
from src.api.chat import router as chat_router
from src.database import engine
from src.models.user import User
from src.models.task import Task
from src.models.conversation import Conversation
from src.utils.logger import logger

# Create tables
from sqlmodel import SQLModel
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    logger.error("DATABASE_URL environment variable is not set!")
    logger.error("Please configure your Neon database connection string.")
    logger.error("Example: DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require")
    raise ValueError("DATABASE_URL environment variable is required")

# Create all tables on startup
logger.info(f"Initializing database: {DATABASE_URL}")
try:
    SQLModel.metadata.create_all(bind=engine)
    logger.info("Database tables created successfully")
except Exception as e:
    logger.error(f"Failed to create database tables: {e}")
    raise

app = FastAPI(title="Todo App API", version="1.0.0")

# Security headers middleware
class SecurityHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response: Response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        response.headers["Strict-Transport-Security"] = "max-age=63072000; includeSubDomains; preload"
        return response

# Add security middleware
app.add_middleware(SecurityHeaderMiddleware)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3001",  # Common Next.js port
        "http://127.0.0.1:3001",
        "http://localhost:3002",  # Another common Next.js port
        "http://127.0.0.1:3002",
        "https://localhost:3000",  # HTTPS variants
        "https://127.0.0.1:3000",
        "https://localhost:3001",
        "https://127.0.0.1:3001",
        "https://localhost:8000",
        "https://127.0.0.1:8000"
    ],  # Allow Next.js dev server and backend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # Security: Limit exposed headers to prevent sensitive data leakage
    expose_headers=["Access-Control-Allow-Origin"]
)

# Trusted Host Middleware - only allow requests from specific hosts in production
# app.add_middleware(TrustedHostMiddleware, allowed_hosts=["yourdomain.com", "www.yourdomain.com"])

# Include routers
app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(tasks_router, prefix="/api", tags=["tasks"])
app.include_router(chat_router, prefix="/api", tags=["chat"])

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the Todo App API"}


@app.get("/verify-db")
def verify_database():
    """Verification endpoint to check if data is being stored in Neon DB"""
    from sqlmodel import Session, select
    from src.models.user import User
    from src.models.conversation import Conversation
    from src.models.task import Task

    with Session(engine) as session:
        # Count existing users, tasks, and conversations
        user_count = len(session.exec(select(User)).all())
        task_count = len(session.exec(select(Task)).all())
        conversation_count = len(session.exec(select(Conversation)).all())

        return {
            "database_connected": True,
            "database_url": DATABASE_URL,  # Show which DB is being used
            "users_count": user_count,
            "tasks_count": task_count,
            "conversations_count": conversation_count,
            "models_loaded": True
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)