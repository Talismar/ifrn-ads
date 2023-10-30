from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.signup import SignupRepository
from cqrs.admin.commands import SignUpPartialUpdateCommand

class SignUpPartialUpdateCommandHandler(ICommandHandler[SignUpPartialUpdateCommand]):
    def __init__(self, session: Session):
        self.repo = SignupRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.update_signup(command.id, command.details)
        return result