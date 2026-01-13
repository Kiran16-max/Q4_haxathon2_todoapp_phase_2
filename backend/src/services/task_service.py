# backend/src/services/task_service.py
from sqlmodel import Session, select
from typing import List, Optional
from uuid import UUID
from src.models.task import Task, TaskCreate, TaskUpdate
from src.utils.logger import logger


def get_tasks_by_user_id(user_id: UUID, session: Session) -> List[Task]:
    """
    Get all tasks for a specific user.

    Args:
        user_id: The ID of the user whose tasks to retrieve
        session: Database session

    Returns:
        List of tasks belonging to the user
    """
    logger.info(f"Retrieving tasks for user {user_id}")
    tasks = session.exec(select(Task).where(Task.user_id == user_id)).all()
    logger.info(f"Found {len(tasks)} tasks for user {user_id}")
    return tasks


def create_task_for_user(task: TaskCreate, user_id: UUID, session: Session) -> Task:
    """
    Create a new task for a specific user.

    Args:
        task: Task creation data
        user_id: The ID of the user creating the task
        session: Database session

    Returns:
        The created task object
    """
    logger.info(f"Creating task for user {user_id}")
    try:
        # Create task with user-provided data and let DB handle timestamps
        db_task = Task(
            title=task.title,
            description=task.description,
            completed=task.completed,
            user_id=user_id
        )
        session.add(db_task)
        session.commit()
        session.refresh(db_task)
        logger.info(f"Task {db_task.id} created for user {user_id}")
        return db_task
    except Exception as e:
        logger.error(f"Error creating task for user {user_id}: {str(e)}")
        session.rollback()
        raise e


def get_task_by_id_and_user(task_id: UUID, user_id: UUID, session: Session) -> Optional[Task]:
    """
    Get a specific task by ID for a specific user.

    Args:
        task_id: The ID of the task to retrieve
        user_id: The ID of the user who owns the task
        session: Database session

    Returns:
        The task if it exists and belongs to the user, None otherwise
    """
    logger.info(f"Retrieving task {task_id} for user {user_id}")
    task = session.get(Task, task_id)
    if task and task.user_id == user_id:
        logger.info(f"Task {task_id} found for user {user_id}")
        return task
    logger.warning(f"Task {task_id} not found or does not belong to user {user_id}")
    return None


def update_task_by_id(task_id: UUID, task_update: TaskUpdate, session: Session) -> Optional[Task]:
    """
    Update a task by ID.

    Args:
        task_id: The ID of the task to update
        task_update: Task update data
        session: Database session

    Returns:
        The updated task object if successful, None otherwise
    """
    logger.info(f"Updating task {task_id}")
    db_task = session.get(Task, task_id)
    if not db_task:
        logger.error(f"Task {task_id} not found for update")
        return None

    # Update task fields
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)

    # Update the updated_at timestamp
    from datetime import datetime
    db_task.updated_at = datetime.utcnow()

    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    logger.info(f"Task {task_id} updated successfully")
    return db_task


def delete_task_by_id(task_id: UUID, session: Session) -> bool:
    """
    Delete a task by ID.

    Args:
        task_id: The ID of the task to delete
        session: Database session

    Returns:
        True if deletion was successful, False otherwise
    """
    logger.info(f"Deleting task {task_id}")
    task = session.get(Task, task_id)
    if not task:
        logger.error(f"Task {task_id} not found for deletion")
        return False

    session.delete(task)
    session.commit()
    logger.info(f"Task {task_id} deleted successfully")
    return True


def toggle_task_completion_service(task_id: UUID, user_id: UUID, session: Session) -> Optional[Task]:
    """
    Toggle the completion status of a task.

    Args:
        task_id: The ID of the task to toggle
        user_id: The ID of the user who owns the task
        session: Database session

    Returns:
        The updated task object if successful, None otherwise
    """
    logger.info(f"Toggling completion status for task {task_id}")
    task = session.get(Task, task_id)
    if not task:
        logger.error(f"Task {task_id} not found for status toggle")
        return None

    # Verify that the task belongs to the user
    if task.user_id != user_id:
        logger.error(f"Task {task_id} does not belong to user {user_id}")
        return None

    task.completed = not task.completed
    from datetime import datetime
    task.updated_at = datetime.utcnow()

    session.add(task)
    session.commit()
    session.refresh(task)
    logger.info(f"Task {task_id} completion status toggled to {task.completed}")
    return task