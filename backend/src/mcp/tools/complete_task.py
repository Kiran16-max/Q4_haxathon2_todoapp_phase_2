# backend/src/mcp/tools/complete_task.py
from sqlmodel import Session
from uuid import UUID
from typing import Dict, Any
from src.services.task_service import get_task_by_id_and_user, update_task_by_id
from src.models.task import TaskUpdate

def complete_task_tool(params: Dict[str, Any], session: Session, user_id: UUID) -> str:
    """
    MCP tool to mark a task as complete or incomplete.
    
    Args:
        params: Parameters for the task completion
            - task_id: ID of the task to update
            - completed: Whether the task is completed (optional, toggles if not provided)
        session: Database session
        user_id: ID of the user who owns the task
        
    Returns:
        Success message with updated task status
    """
    task_id = params.get("task_id")
    if not task_id:
        raise ValueError("Task ID is required to complete a task")
    
    # Get the task
    task = get_task_by_id_and_user(task_id, user_id, session)
    if not task:
        raise ValueError(f"Task with ID {task_id} not found or not owned by user")
    
    # Determine new completion status
    completed = params.get("completed")
    if completed is None:
        # Toggle the status if not specified
        completed = not task.completed
    else:
        # Use the provided status
        completed = bool(completed)
    
    # Update the task
    task_update = TaskUpdate(completed=completed)
    updated_task = update_task_by_id(task_id, task_update, session)
    
    if updated_task:
        status = "completed" if updated_task.completed else "incomplete"
        return f"Task '{updated_task.title}' has been marked as {status}."
    else:
        raise ValueError("Failed to update task")