# backend/migrations/initial_migration.py
"""
Initial database migration script for the Todo App
This script creates the initial tables for users, tasks, and conversations
"""

from sqlmodel import SQLModel
from src.database import engine
from src.models.user import User
from src.models.task import Task
from src.models.conversation import Conversation

def run_migrations():
    """
    Creates all tables in the database based on the SQLModel definitions
    """
    print("Running initial database migration...")
    SQLModel.metadata.create_all(engine)
    print("Database migration completed successfully!")

if __name__ == "__main__":
    run_migrations()