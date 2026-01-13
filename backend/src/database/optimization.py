# backend/src/database/optimization.py
from sqlmodel import create_engine, Session
from src.models.user import User
from src.models.task import Task
from src.models.conversation import Conversation

def add_indexes(engine):
    """
    Add database indexes to optimize query performance.
    This function adds indexes to commonly queried columns.
    """
    with Session(engine) as session:
        # Add indexes for Task model
        # Index on user_id for efficient user-based queries
        session.exec("CREATE INDEX IF NOT EXISTS idx_task_user_id ON task (user_id);")
        
        # Index on (user_id, completed) for filtered queries
        session.exec("CREATE INDEX IF NOT EXISTS idx_task_user_completed ON task (user_id, completed);")
        
        # Index on created_at for chronological queries
        session.exec("CREATE INDEX IF NOT EXISTS idx_task_created_at ON task (created_at);")
        
        # Add indexes for Conversation model
        # Index on user_id for efficient user-based queries
        session.exec("CREATE INDEX IF NOT EXISTS idx_conversation_user_id ON conversation (user_id);")
        
        # Index on created_at for chronological queries
        session.exec("CREATE INDEX IF NOT EXISTS idx_conversation_created_at ON conversation (created_at);")
        
        session.commit()
        print("Database indexes added successfully!")


def optimize_database_queries():
    """
    This function contains recommendations for optimizing database queries.
    Actual implementation would depend on the specific ORM and database being used.
    """
    print("Query optimization recommendations:")
    print("1. Use select statements with specific columns instead of SELECT *")
    print("2. Use pagination for large result sets")
    print("3. Leverage the indexes created in add_indexes()")
    print("4. Use connection pooling")
    print("5. Consider caching frequently accessed data")
    print("6. Use eager loading to prevent N+1 query problems")


if __name__ == "__main__":
    from src.database import engine
    add_indexes(engine)
    optimize_database_queries()