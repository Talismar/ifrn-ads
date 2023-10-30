from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.attendance_member import AttendanceMemberRepository
from cqrs.attendance_member.commands import AttendanceMemberPartialUpdateCommand

class AttendanceMemberPartialUpdateCommandHandler(ICommandHandler[AttendanceMemberPartialUpdateCommand]):
    def __init__(self, session: Session):
        self.repo = AttendanceMemberRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.partial_update(command.id, command.details)
        return result