from app.repositories.user_repository import UserRepository
from fastapi import HTTPException, Response
from app.utils.hash_password import hash_password
from sqlalchemy.exc import IntegrityError


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def list_all(self):
        return self.user_repository.list_all()

    def create(self, data):
        if data.password != data.password_confirm:
            raise HTTPException(
                status_code=400,
                detail="Passwords do not match",
            )

        del data.password_confirm

        data.password = hash_password(data.password)

        try:
            return self.user_repository.create(data)
        except IntegrityError:
            raise HTTPException(
                status_code=409,
                detail="Account already exists",
            )

    def delete(self, id):
        try:
            self.user_repository.delete(id)
            return Response(status_code=204)
        except:
            raise HTTPException(status_code=400, detail="Error deleting account")

    def get_one(self, id):
        return self.user_repository.get_by_id(id)

    def partial_update(self, id, data):
        return self.user_repository.partial_update(id, data)
