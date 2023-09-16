from .base_model import BaseModel
from .mixin import CommonMixin, TimestampMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Enum as SQLAlchemyEnum, ForeignKey
from enum import Enum


class TaskStatusEnum(str, Enum):
    TO_DO = "TO DO"
    DOING = "DOING"
    DONE = "DONE"


class Task(CommonMixin, TimestampMixin, BaseModel):
    name: Mapped[str] = mapped_column(String(length=220))
    description: Mapped[str]
    status: Mapped[Enum] = mapped_column(
        SQLAlchemyEnum(TaskStatusEnum), default=TaskStatusEnum.TO_DO
    )
    created_by_id: Mapped[int] = mapped_column(
        ForeignKey(column="user.id", ondelete="CASCADE")
    )
    created_by: Mapped["User"] = relationship(back_populates="tasks")
