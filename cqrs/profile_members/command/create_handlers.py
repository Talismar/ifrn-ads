from sqlalchemy.orm import Session
from cqrs.admin.handlers import ICommandHandler
from repository.sqlalchemy.profile_members import ProfileMembersRepository
from cqrs.profile_members.commands import ProfileMembersCommand

class ProfileMembersCreateCommandHandler(ICommandHandler[ProfileMembersCommand]):
    def __init__(self, session: Session):
        self.repo = ProfileMembersRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.insert(command.details)
        return result
