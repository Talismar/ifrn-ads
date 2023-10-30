from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.login.commands import LoginUpdateCommand

class LoginPartialUpdateCommandHandler(ICommandHandler[LoginUpdateCommand]):
    def __init__(self, session: Session):
        self.repo = LoginRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.update_login(command.id, command.details)
        return result