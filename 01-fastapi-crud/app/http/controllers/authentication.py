from app.services.factories.make_authentication_service import (
    make_authentication_service,
)
from fastapi import Depends, Request
from app.services.authentication import AuthenticationService
from starlette.datastructures import UploadFile
from app.schemas.authentication import AuthenticationRefreshTokenPostResponseSchema


async def authentication_token(
    request: Request,
    authentication_service: AuthenticationService = Depends(
        make_authentication_service
    ),
):
    email: None | str | UploadFile = None
    password: None | str | UploadFile = None

    async with request.form() as form:
        email = form.get("username", None)
        password = form.get("password", None)

    if email is None and password is None:
        data_json = await request.json()

        email = data_json["email"]
        password = data_json["password"]

    return authentication_service.token(email, password)


def refresh_token(
    data: AuthenticationRefreshTokenPostResponseSchema,
    authentication_service: AuthenticationService = Depends(
        make_authentication_service
    ),
):
    return authentication_service.refresh_token(data.refresh_token)
