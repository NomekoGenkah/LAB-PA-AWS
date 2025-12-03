from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional, List


class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    parent_id: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    parent_id: Optional[int] = None


class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class TaskWithSubtasks(Task):
    subtasks: List["TaskWithSubtasks"] = []
    
    model_config = ConfigDict(from_attributes=True)
