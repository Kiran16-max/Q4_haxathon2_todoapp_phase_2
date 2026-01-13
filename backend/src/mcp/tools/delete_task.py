# backend/src/mcp/tools/delete_task.py
from sqlmodel import Session
from uuid import UUID
from typing import Dict, Any
from src.services.task_service import get_task_by_id_and_user, delete_task_by_id

def delete_task_tool(params: Dict[str, Any], session: Session, user_id: UUID) -> str:
    """
    MCP tool to delete a task for the user.
    
    Args:
        params: Parameters for the task deletion
            - task_id: ID of the task to delete
        session: Database session
        user_id: ID of the user who owns the task
        
    Returns:
        Success message confirming deletion
    """
    task_id = params.get("task_id")
    if not task_id:
        raise ValueError("Task ID is required to delete a task")
    
    # Get the task to verify ownership
    task = get_task_by_id_and_user(task_id, user_id, session)
    if not task:
        raise ValueError(f"Task with ID {task_id} not found or not owned by user")
    
    # Delete the task
    success = delete_task_by_id(task_id, session)
    
    if success:
        return f"Task '{task.title}' has been deleted successfully."
    else:
        raise ValueError("Failed to delete task")