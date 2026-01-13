# backend/src/mcp/tools/add_task.py
from sqlmodel import Session
from uuid import UUID
from typing import Dict, Any
from src.services.task_service import create_task_for_user
from src.models.task import TaskCreate

def add_task_tool(params: Dict[str, Any], session: Session, user_id: UUID) -> str:
    """
    MCP tool to add a new task for the user.
    
    Args:
        params: Parameters for the task creation
            - title: Task title (required)
            - description: Task description (optional)
        session: Database session
        user_id: ID of the user creating the task
        
    Returns:
        Success message with task details
    """
    title = params.get("title")
    if not title:
        raise ValueError("Title is required to create a task")
    
    description = params.get("description", "")
    
    # Create task using the service
    task_create = TaskCreate(title=title, description=description)
    new_task = create_task_for_user(task_create, user_id, session)
    
    return f"Task '{new_task.title}' has been created successfully."