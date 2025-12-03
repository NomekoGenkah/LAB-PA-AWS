from sqlalchemy.orm import Session, joinedload
from . import models, schemas
from typing import List, Optional


def get_task(db: Session, task_id: int) -> Optional[models.Task]:
    """Get a single task by ID"""
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def get_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.Task]:
    """Get all tasks (paginated)"""
    return db.query(models.Task).offset(skip).limit(limit).all()


def get_root_tasks(db: Session, skip: int = 0, limit: int = 100) -> List[models.Task]:
    """Get only root tasks (tasks without parent)"""
    return db.query(models.Task).filter(models.Task.parent_id.is_(None)).offset(skip).limit(limit).all()


def get_task_with_subtasks(db: Session, task_id: int) -> Optional[models.Task]:
    """Get a task with all its subtasks recursively loaded"""
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        # Load subtasks recursively
        _load_subtasks_recursive(db, task)
    return task


def _load_subtasks_recursive(db: Session, task: models.Task):
    """Helper function to recursively load all subtasks"""
    # Explicitly load subtasks
    db.refresh(task, ["subtasks"])
    for subtask in task.subtasks:
        _load_subtasks_recursive(db, subtask)


def create_task(db: Session, task: schemas.TaskCreate) -> models.Task:
    """Create a new task"""
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def update_task(db: Session, task_id: int, task_update: schemas.TaskUpdate) -> Optional[models.Task]:
    """Update an existing task"""
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_task, field, value)
    
    db.commit()
    db.refresh(db_task)
    return db_task


def delete_task(db: Session, task_id: int) -> bool:
    """Delete a task and all its subtasks (cascade)"""
    db_task = get_task(db, task_id)
    if not db_task:
        return False
    
    # Delete all subtasks first (recursive)
    _delete_subtasks_recursive(db, task_id)
    
    # Delete the task itself
    db.delete(db_task)
    db.commit()
    return True


def _delete_subtasks_recursive(db: Session, parent_id: int):
    """Helper function to recursively delete all subtasks"""
    subtasks = db.query(models.Task).filter(models.Task.parent_id == parent_id).all()
    for subtask in subtasks:
        _delete_subtasks_recursive(db, subtask.id)
        db.delete(subtask)
