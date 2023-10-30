from typing import TypeVar, Generic

T = TypeVar("T")

class IQueryHandler(Generic[T]):
    def handle(self, query: T):
        raise NotImplementedError()

class ICommandHandler(Generic[T]):
    def handle(self, command: T):
        raise NotImplementedError()