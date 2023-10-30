from sqlalchemy.orm import Session
from cqrs.admin.handlers import ICommandHandler
from repository.sqlalchemy.profile_trainers import ProfileTrainersRepository
from cqrs.profile_trainers.commands import ProfileTrainersCommand

class ProfileTrainersCreateCommandHandler(ICommandHandler[ProfileTrainersCommand]):
    def __init__(self, session: Session):
        self.repo = ProfileTrainersRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.insert(command.details)
        return result
