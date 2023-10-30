from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.profile_trainers import ProfileTrainersRepository
from cqrs.profile_trainers.commands import ProfileTrainersPartialUpdateCommand

class ProfileTrainersPartialUpdateCommandHandler(ICommandHandler[ProfileTrainersPartialUpdateCommand]):
    def __init__(self, session: Session):
        self.repo = ProfileTrainersRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.partial_update(command.id, command.details)
        return result