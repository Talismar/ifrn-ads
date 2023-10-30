from sqlalchemy.orm import Session
from cqrs.login.handlers import IQueryHandler
from cqrs.profile_members.queries import ProfileMembersListQuery, ProfileMembersOneQuery
from repository.sqlalchemy.profile_members import ProfileMembersRepository


class ProfileMembersGetAllQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo = ProfileMembersRepository(session)
        self.query = ProfileMembersListQuery()

    def handle(self):
        data = self.repo.get_all()
        self.query.records = data
        return self.query
    

class ProfileMembersGetByIdQueryHandler(IQueryHandler[ProfileMembersOneQuery]):
    def __init__(self, session: Session):
        self.repo = ProfileMembersRepository(session)
        self.query: ProfileMembersOneQuery | None = None

    def handle(self, query):
        self.query = query
        data = self.repo.get_by_id(query.id)
        self.query.records = data
        return self.query