from sqlalchemy.orm import Session
from cqrs.admin.handlers import ICommandHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.gym_class.commands import GymClassCommand

class GymClassCreateCommandHandler(ICommandHandler[GymClassCommand]):
    def __init__(self, session: Session):
        self.repo = GymClassRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.insert(command.details)
        return result
