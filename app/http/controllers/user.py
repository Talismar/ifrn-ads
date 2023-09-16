from app.services.factories.make_user_service import make_user_service
from fastapi import Depends, Query
from app.services.user import UserService
from app.schemas.user import (
    UserPostRequestSchema,
    UserPartialUpdateRequestSchema,
    UserLoginPostRequestSchema,
)


def list_all(user_service: UserService = Depends(make_user_service)):
    return user_service.list_all()


def get_one(user_id: int, user_service: UserService = Depends(make_user_service)):
    return user_service.get_one(user_id)


def create(
    data: UserPostRequestSchema, user_service: UserService = Depends(make_user_service)
):
    return user_service.create(data)


def delete(user_id: int, user_service: UserService = Depends(make_user_service)):
    return user_service.delete(user_id)


def partial_update(
    user_id: int,
    form: UserPartialUpdateRequestSchema,
    user_service: UserService = Depends(make_user_service),
):
    return user_service.partial_update(user_id, form)
