from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from app.models.task import TaskStatusEnum
from .user import UserSchema


class TaskBaseSchema(BaseModel):
    name: str
    description: str


class TaskSchema(TaskBaseSchema):
    id: int
    status: TaskStatusEnum
    created_at: datetime
    updated_at: datetime
    created_by: UserSchema


class TaskPostRequestSchema(TaskBaseSchema):
    pass
    # created_by_id: int = Field(ge=1) - current user depends


class TaskPartialUpdateRequestSchema(TaskBaseSchema):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatusEnum] = None
