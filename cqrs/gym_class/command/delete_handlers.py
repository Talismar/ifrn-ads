from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.gym_class.commands import GymClassDeleteCommand

class GymClassDeleteCommandHandler(ICommandHandler[GymClassDeleteCommand]):
    def __init__(self, session: Session):
        self.repo = GymClassRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.delete(command.id)
        return result