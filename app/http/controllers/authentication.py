from app.services.factories.make_authentication_service import (
    make_authentication_service,
)
from fastapi import Depends, Request, BackgroundTasks, HTTPException
from app.services.authentication import AuthenticationService
from starlette.datastructures import UploadFile
from app.schemas.authentication import AuthenticationRefreshTokenPostResponseSchema
from app.background_tasks import authenticated_user_audit


async def authentication_token(
    request: Request,
    background_tasks: BackgroundTasks,
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

    hasError = False
    try:
        return authentication_service.token(email, password)
    except HTTPException as error:
        hasError = True
        raise error
    finally:
        if not hasError:
            background_tasks.add_task(authenticated_user_audit, email)


def refresh_token(
    data: AuthenticationRefreshTokenPostResponseSchema,
    authentication_service: AuthenticationService = Depends(
        make_authentication_service
    ),
):
    return authentication_service.refresh_token(data.refresh_token)
