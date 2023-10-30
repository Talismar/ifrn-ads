from sqlalchemy.orm import Session
from cqrs.admin.handlers import ICommandHandler
from repository.sqlalchemy.attendance_member import AttendanceMemberRepository
from cqrs.attendance_member.commands import AttendanceMemberCommand

class AttendanceMemberCreateCommandHandler(ICommandHandler[AttendanceMemberCommand]):
    def __init__(self, session: Session):
        self.repo = AttendanceMemberRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.insert(command.details)
        return result
