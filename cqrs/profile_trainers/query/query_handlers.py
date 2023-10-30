from sqlalchemy.orm import Session
from cqrs.login.handlers import IQueryHandler
from cqrs.profile_trainers.queries import ProfileTrainersListQuery, ProfileTrainersOneQuery
from repository.sqlalchemy.profile_trainers import ProfileTrainersRepository


class ProfileTrainersGetAllQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo = ProfileTrainersRepository(session)
        self.query = ProfileTrainersListQuery()

    def handle(self):
        data = self.repo.get_all()
        self.query.records = data
        return self.query
    

class ProfileTrainersGetByIdQueryHandler(IQueryHandler[ProfileTrainersOneQuery]):
    def __init__(self, session: Session):
        self.repo = ProfileTrainersRepository(session)
        self.query: ProfileTrainersOneQuery | None = None

    def handle(self, query):
        self.query = query
        data = self.repo.get_by_id(query.id)
        self.query.records = data
        return self.query