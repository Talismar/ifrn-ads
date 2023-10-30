from sqlalchemy.orm import Session
from cqrs.login.handlers import ICommandHandler
from repository.sqlalchemy.attendance_member import AttendanceMemberRepository
from cqrs.attendance_member.commands import AttendanceMemberDeleteCommand

class AttendanceMemberDeleteCommandHandler(ICommandHandler[AttendanceMemberDeleteCommand]):
    def __init__(self, session: Session):
        self.repo = AttendanceMemberRepository(session)

    def handle(self, command) -> bool:
        result = self.repo.delete(command.id)
        return result