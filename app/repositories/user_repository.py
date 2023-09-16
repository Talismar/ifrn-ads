from typing import Generic, TypeVar, Any
from ..models.user import User
from abc import ABC, abstractmethod
from app.schemas.user import UserPartialUpdateRequestSchema, UserSchema

T = TypeVar("T")


class UserRepository(ABC, Generic[T]):
    def __init__(self, db: T) -> None:
        self._db = db

    @abstractmethod
    def list_all(self) -> list[UserSchema]:
        pass

    @abstractmethod
    def create(self, user: Any) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User:
        pass

    @abstractmethod
    def get_by_email(self, user_id: str) -> User | None:
        pass

    @abstractmethod
    def partial_update(
        self, user_id: int, data: UserPartialUpdateRequestSchema
    ) -> User:
        pass

    def save(self):
        self._db.commit()

    @abstractmethod
    def delete(self, id: int):
        ...
