from sqlalchemy.orm import Session
from cqrs.login.handlers import IQueryHandler
from cqrs.admin.queries import SignUpListQuery, SignUpOneQuery, LoginMemberJoinQuery, AttendanceMemberJoinQuery
from repository.sqlalchemy.signup import SignupRepository, LoginMemberRepository, MemberAttendanceRepository


class SignUpGetAllQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo = SignupRepository(session)
        self.query = SignUpListQuery()

    def handle(self):
        data = self.repo.get_all_signup()
        self.query.records = data
        return self.query
    

class SignUpGetByIdQueryHandler(IQueryHandler[SignUpOneQuery]):
    def __init__(self, session: Session):
        self.repo = SignupRepository(session)
        self.query: SignUpOneQuery | None = None

    def handle(self, query):
        self.query = query
        data = self.repo.get_signup(query.id)
        self.query.records = data
        return self.query
    
class LoginMemberJoinQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo = LoginMemberRepository(session)
        self.query = LoginMemberJoinQuery()

    def handle(self):
        data = self.repo.join_login_members()
        self.query.records = data
        return self.query
    

class MemberAttendanceJoinQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo = MemberAttendanceRepository(session)
        self.query = AttendanceMemberJoinQuery()

    def handle(self):
        data = self.repo.join_member_attendance()
        self.query.records = data
        return self.query