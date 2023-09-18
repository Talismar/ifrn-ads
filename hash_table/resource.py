from abc import ABC


class Resource(ABC):
    def __init__(self, register: int) -> None:
        self.register = register
