from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.login import LoginRepository
from cqrs.login.commands import LoginCommand

class LoginCreateCommandHandler(ICommandHandler[LoginCommand]):
    def __init__(self, session: Session):
        self.repo = LoginRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.insert_login(command.details)
        return result