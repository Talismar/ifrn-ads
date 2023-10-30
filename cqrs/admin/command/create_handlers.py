from sqlalchemy.orm import Session
from cqrs.admin.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.admin.commands import SignUpCommand

class SignUpCreateCommandHandler(ICommandHandler[SignUpCommand]):
    def __init__(self, session: Session):
        self.repo = SignupRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.insert_signup(command.details)
        return result
