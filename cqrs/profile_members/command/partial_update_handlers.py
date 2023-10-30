from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.profile_members import ProfileMembersRepository
from cqrs.profile_members.commands import ProfileMembersPartialUpdateCommand

class ProfileMembersPartialUpdateCommandHandler(ICommandHandler[ProfileMembersPartialUpdateCommand]):
    def __init__(self, session: Session):
        self.repo = ProfileMembersRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.partial_update(command.id, command.details)
        return result