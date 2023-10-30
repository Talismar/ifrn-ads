from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.profile_members import ProfileMembersRepository
from cqrs.profile_members.commands import ProfileMembersDeleteCommand

class ProfileMembersDeleteCommandHandler(ICommandHandler[ProfileMembersDeleteCommand]):
    def __init__(self, session: Session):
        self.repo = ProfileMembersRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.delete(command.id)
        return result