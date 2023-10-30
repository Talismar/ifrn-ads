from sqlalchemy.orm import Session
from cqrs.login.handlers import IQueryHandler
from cqrs.attendance_member.queries import AttendanceMemberListQuery, AttendanceMemberOneQuery
from repository.sqlalchemy.attendance_member import AttendanceMemberRepository


class AttendanceMemberGetAllQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo = AttendanceMemberRepository(session)
        self.query = AttendanceMemberListQuery()

    def handle(self):
        data = self.repo.get_all()
        self.query.records = data
        return self.query
    

class AttendanceMemberGetByIdQueryHandler(IQueryHandler[AttendanceMemberOneQuery]):
    def __init__(self, session: Session):
        self.repo = AttendanceMemberRepository(session)
        self.query: AttendanceMemberOneQuery | None = None

    def handle(self, query):
        self.query = query
        data = self.repo.get_by_id(query.id)
        self.query.records = data
        return self.query