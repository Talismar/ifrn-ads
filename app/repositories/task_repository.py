from typing import Generic, TypeVar, Any
from ..models.task import Task
from ..models import User
from abc import ABC, abstractmethod
from app.schemas.task import TaskPostRequestSchema, TaskSchema

T = TypeVar("T")


class TaskRepository(ABC, Generic[T]):
    def __init__(self, db: T) -> None:
        self._db = db

    @abstractmethod
    def list_all(self) -> list[TaskSchema]:
        pass

    @abstractmethod
    def create(self, user: TaskPostRequestSchema, created_by: User) -> Task:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Task | None:
        pass

    @abstractmethod
    def get_by_email(self, user_id: str) -> Task:
        pass

    @abstractmethod
    def partial_update(self, user_id: int, data) -> Task:
        pass

    def save(self):
        self._db.commit()

    @abstractmethod
    def delete(self, id: int):
        ...
