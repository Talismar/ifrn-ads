from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.gym_class import GymClassRepository
from cqrs.gym_class.commands import GymClassPartialUpdateCommand

class GymClassPartialUpdateCommandHandler(ICommandHandler[GymClassPartialUpdateCommand]):
    def __init__(self, session: Session):
        self.repo = GymClassRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.partial_update(command.id, command.details)
        return result