from app.schemas.user import UserPostRequestSchema
from sqlalchemy.orm import Session
from app.models import User
from app.repositories.user_repository import UserRepository


class SqlalchemyUserRepository(UserRepository[Session]):
    def list_all(self):
        return self._db.query(User).all()

    def create(self, user: UserPostRequestSchema):
        db_user = User(**user.model_dump())

        self._db.add(db_user)
        self._db.commit()
        self._db.refresh(db_user)

        return db_user

    def get_by_id(self, id: int):
        return self._db.query(User).filter_by(id=id).first()

    def get_by_email(self, email: str):
        return self._db.query(User).filter_by(email=email).first()

    def partial_update(self, id: int, data):
        db_user = self._db.query(User).filter_by(id=id).first()

        for field, value in data.model_dump().items():
            if value is not None:
                setattr(db_user, field, value)

        self._db.commit()
        return db_user

    def delete(self, id):
        obj = self._db.query(User).get(id)
        self._db.delete(obj)
        self._db.commit()
