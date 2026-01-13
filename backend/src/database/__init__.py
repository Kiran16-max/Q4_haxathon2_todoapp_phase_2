from .database import engine, get_session, SessionLocal
import os

DATABASE_URL = os.getenv("DATABASE_URL")