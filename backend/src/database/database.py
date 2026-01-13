from sqlmodel import create_engine, Session
from sqlalchemy import event
from sqlalchemy.engine import URL
from typing import Generator
import os

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

# Handle Neon connection string format
if DATABASE_URL and DATABASE_URL.startswith("neon://"):
    # Convert neon:// to postgresql+asyncpg:// format
    DATABASE_URL = DATABASE_URL.replace("neon://", "postgresql://", 1)

# Check if running in production-like environment
if not DATABASE_URL:
    # Raise an error if DATABASE_URL is not set in production
    import sys
    print("ERROR: DATABASE_URL environment variable is not set.")
    print("Please configure your Neon database connection string.")
    print("Example: DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require")
    sys.exit(1)

# Create sync engine (since SQLModel uses sync operations)
engine = create_engine(
    DATABASE_URL,
    echo=False,  # Set to True for SQL debug output
    pool_pre_ping=True,  # Verify connections before use
    connect_args={
        "connect_timeout": 10,
    } if "postgresql" in DATABASE_URL else {}  # Only use connect_args for PostgreSQL
)

# Create a sessionmaker for compatibility if needed
SessionLocal = Session


def get_session() -> Generator[Session, None, None]:
    """
    Dependency to get a database session
    """
    with Session(engine) as session:
        yield session