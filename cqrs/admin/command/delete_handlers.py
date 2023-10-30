from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.admin.commands import SignUpDeleteCommand

class SignUpDeleteCommandHandler(ICommandHandler[SignUpDeleteCommand]):
    def __init__(self, session: Session):
        self.repo = SignupRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.delete_signup(command.id)
        return result