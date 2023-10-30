from sqlalchemy.orm import Session
from cqrs.login.handlers import IQueryHandler
from cqrs.gym_class.queries import GymClassListQuery, GymClassOneQuery
from repository.sqlalchemy.gym_class import GymClassRepository


class GymClassGetAllQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo = GymClassRepository(session)
        self.query = GymClassListQuery()

    def handle(self):
        data = self.repo.get_all()
        self.query.records = data
        return self.query
    

class GymClassGetByIdQueryHandler(IQueryHandler[GymClassOneQuery]):
    def __init__(self, session: Session):
        self.repo = GymClassRepository(session)
        self.query: GymClassOneQuery | None = None

    def handle(self, query):
        self.query = query
        data = self.repo.get_by_id(query.id)
        self.query.records = data
        return self.query