# backend/src/mcp/tools/list_tasks.py
from sqlmodel import Session
from uuid import UUID
from typing import Dict, Any
from src.services.task_service import get_tasks_by_user_id

def list_tasks_tool(params: Dict[str, Any], session: Session, user_id: UUID) -> str:
    """
    MCP tool to list all tasks for the user.
    
    Args:
        params: Parameters for the task listing (currently unused)
        session: Database session
        user_id: ID of the user whose tasks to list
        
    Returns:
        Formatted string with task details
    """
    # Get tasks for the user
    tasks = get_tasks_by_user_id(user_id, session)
    
    if not tasks:
        return "You have no tasks at the moment."
    
    # Format tasks for display
    task_list = []
    for i, task in enumerate(tasks, 1):
        status = "✓" if task.completed else "○"
        task_list.append(f"{i}. [{status}] {task.title}")
    
    return "\n".join(task_list)