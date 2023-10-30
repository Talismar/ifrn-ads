from sqlalchemy.orm import Session
from cqrs.login.handlers import IQueryHandler
from cqrs.login.queries import LoginListQuery, LoginOneQuery
from repository.sqlalchemy.login import LoginRepository


class LoginGetAllQueryHandler(IQueryHandler):
    def __init__(self, session: Session):
        self.repo: LoginRepository = LoginRepository(session)
        self.query = LoginListQuery()

    def handle(self) -> LoginListQuery:
        data = self.repo.get_all_login()
        self.query.records = data
        return self.query
    

class LoginGetByIdQueryHandler(IQueryHandler[LoginOneQuery]):
    def __init__(self, session: Session):
        self.repo: LoginRepository = LoginRepository(session)
        self.query: LoginOneQuery | None = None

    def handle(self, query):
        self.query = query
        data = self.repo.get_login(query.id)
        self.query.records = data
        return self.query