# backend/src/api/tasks.py
from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session, select
from typing import List
from uuid import UUID
from src.database import engine
from src.models.task import Task, TaskCreate, TaskRead, TaskUpdate
from src.models.user import User
from src.utils.jwt_handler import get_current_user
from src.services.task_service import (
    get_tasks_by_user_id,
    create_task_for_user,
    get_task_by_id_and_user,
    update_task_by_id,
    delete_task_by_id,
    toggle_task_completion_service
)

router = APIRouter()

def get_session():
    with Session(engine) as session:
        yield session

@router.get("/tasks", response_model=List[TaskRead])
def read_tasks(
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Get tasks for the current user only
    tasks = get_tasks_by_user_id(current_user.id, session)
    return tasks

@router.post("/tasks")
def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Create task for the current user
    try:
        db_task = create_task_for_user(task, current_user.id, session)
        return {"status": "success", "task": db_task}
    except Exception as e:
        # Log the error
        from src.utils.logger import logger
        logger.error(f"Error creating task: {str(e)}")

        # Return error response
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail={"status": "error", "message": str(e)})

@router.get("/tasks/{task_id}", response_model=TaskRead)
def read_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Get specific task for the current user
    task = get_task_by_id_and_user(task_id, current_user.id, session)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.put("/tasks/{task_id}", response_model=TaskRead)
def update_task(
    task_id: UUID,
    task: TaskUpdate,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Update specific task for the current user
    db_task = get_task_by_id_and_user(task_id, current_user.id, session)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Update task using service
    updated_task = update_task_by_id(task_id, task, session)
    if not updated_task:
        raise HTTPException(status_code=500, detail="Could not update task")

    return updated_task

@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Delete specific task for the current user
    db_task = get_task_by_id_and_user(task_id, current_user.id, session)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")

    success = delete_task_by_id(task_id, session)
    if not success:
        raise HTTPException(status_code=500, detail="Could not delete task")

    return {"message": "Task deleted successfully"}

@router.patch("/tasks/{task_id}/complete", response_model=TaskRead)
def toggle_task_completion_endpoint(
    task_id: UUID,
    current_user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    # Toggle completion status for the current user's task
    task = get_task_by_id_and_user(task_id, current_user.id, session)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = toggle_task_completion_service(task_id, current_user.id, session)
    if not updated_task:
        raise HTTPException(status_code=500, detail="Could not update task status")

    return updated_task