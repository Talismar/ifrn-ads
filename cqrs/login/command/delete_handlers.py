from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.login.commands import LoginDeleteCommand

class LoginDeleteCommandHandler(ICommandHandler[LoginDeleteCommand]):
    def __init__(self, session: Session):
        self.repo = LoginRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.delete_login(command.id)
        return result