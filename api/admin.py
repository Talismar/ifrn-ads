from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from dependencies import database_session
from domain.request.signup import SignupReq, SignupSchema
from typing import List
from cqrs.admin.command.create_handlers import (
    SignUpCreateCommandHandler, 
    SignUpCommand
)
from cqrs.admin.command.partial_update_handlers import (
    SignUpPartialUpdateCommandHandler, 
    SignUpPartialUpdateCommand
)
from cqrs.admin.command.delete_handlers import (
    SignUpDeleteCommandHandler, 
    SignUpDeleteCommand
)
from cqrs.admin.query.query_handlers import (
    SignUpGetAllQueryHandler,
    LoginMemberJoinQueryHandler,
    SignUpGetByIdQueryHandler,
    MemberAttendanceJoinQueryHandler,
    SignUpOneQuery,
)

router = APIRouter(tags=["Admin"])

@router.post("/signup/add", status_code=201)
def add_signup(data: SignupReq, session: Session = Depends(database_session)):
    handler = SignUpCreateCommandHandler(session)
    command = SignUpCommand()
    command.details = data.model_dump()
    result = handler.handle(command)
    if result == True:
        return data
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)


@router.get("/signup/list", response_model=List[SignupSchema])
def list_signup(session: Session = Depends(database_session)):
    handler = SignUpGetAllQueryHandler(session)
    result = handler.handle()
    return result.records


@router.patch("/signup/update")
def update_signup(id: int, req: SignupReq, session: Session = Depends(database_session)):
    signup_dict = req.model_dump(exclude_unset=True)
    handler = SignUpPartialUpdateCommandHandler(session)
    command = SignUpPartialUpdateCommand(id)
    command.details = signup_dict
    result = handler.handle(command)

    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/signup/delete/{id}")
def delete_signup(id: int, session: Session = Depends(database_session)):
    handler = SignUpDeleteCommandHandler(session)
    command = SignUpDeleteCommand(id)
    result = handler.handle(command)
    if result:
        return JSONResponse(content={'message': 'profile deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete profile error'}, status_code=500)


@router.get("/signup/list/{id}", response_model=SignupSchema)
def get_signup(id: int, session: Session = Depends(database_session)):
    handler = SignUpGetByIdQueryHandler(session)
    query = SignUpOneQuery(id)
    result = handler.handle(query)
    return result.records

@router.get("/login/memberslist")
def get_join_login_members(session: Session = Depends(database_session)):
    handler = LoginMemberJoinQueryHandler(session)
    result = handler.handle()
    return result.records


@router.get("/member/attendance")
def get_join_member_attendance(session: Session = Depends(database_session)):
    handler = MemberAttendanceJoinQueryHandler(session)
    result = handler.handle()
    return result.records
