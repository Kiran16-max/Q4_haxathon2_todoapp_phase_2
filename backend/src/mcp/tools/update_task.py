# backend/src/mcp/tools/update_task.py
from sqlmodel import Session
from uuid import UUID
from typing import Dict, Any
from src.services.task_service import get_task_by_id_and_user, update_task_by_id
from src.models.task import TaskUpdate

def update_task_tool(params: Dict[str, Any], session: Session, user_id: UUID) -> str:
    """
    MCP tool to update a task for the user.
    
    Args:
        params: Parameters for the task update
            - task_id: ID of the task to update
            - title: New title (optional)
            - description: New description (optional)
            - completed: New completion status (optional)
        session: Database session
        user_id: ID of the user who owns the task
        
    Returns:
        Success message with updated task details
    """
    task_id = params.get("task_id")
    if not task_id:
        raise ValueError("Task ID is required to update a task")
    
    # Get the task to verify ownership
    task = get_task_by_id_and_user(task_id, user_id, session)
    if not task:
        raise ValueError(f"Task with ID {task_id} not found or not owned by user")
    
    # Prepare update data
    update_data = {}
    if "title" in params:
        update_data["title"] = params["title"]
    if "description" in params:
        update_data["description"] = params["description"]
    if "completed" in params:
        update_data["completed"] = params["completed"]
    
    if not update_data:
        raise ValueError("At least one field (title, description, or completed) must be provided for update")
    
    # Create TaskUpdate object
    task_update = TaskUpdate(**update_data)
    
    # Update the task
    updated_task = update_task_by_id(task_id, task_update, session)
    
    if updated_task:
        return f"Task '{updated_task.title}' has been updated successfully."
    else:
        raise ValueError("Failed to update task")