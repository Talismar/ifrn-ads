from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from dependencies import database_session
from domain.request.attendance import AttendanceMemberReq, AttendanceMemberSchema
from cqrs.attendance_member.command.create_handlers import (
    AttendanceMemberCreateCommandHandler, 
    AttendanceMemberCommand
)
from cqrs.attendance_member.command.partial_update_handlers import (
    AttendanceMemberPartialUpdateCommandHandler, 
    AttendanceMemberPartialUpdateCommand
)
from cqrs.attendance_member.command.delete_handlers import (
    AttendanceMemberDeleteCommandHandler, 
    AttendanceMemberDeleteCommand
)
from cqrs.attendance_member.query.query_handlers import (
    AttendanceMemberGetAllQueryHandler,
    AttendanceMemberGetByIdQueryHandler,
    AttendanceMemberOneQuery
)

router = APIRouter(prefix="/attendance_member", tags=["Attendance Member"])

@router.post("/create")
def create(data: AttendanceMemberReq, session: Session = Depends(database_session)):
    handler = AttendanceMemberCreateCommandHandler(session)
    command = AttendanceMemberCommand()
    command.details = data.model_dump()
    result = handler.handle(command)

    if result == True:
        return JSONResponse(content=jsonable_encoder(data), status_code=201)
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)


@router.get("/list", response_model=List[AttendanceMemberSchema])
def list(session: Session = Depends(database_session)):
    handler = AttendanceMemberGetAllQueryHandler(session)
    result = handler.handle()
    return result.records


@router.get("/detail/{id}", response_model=AttendanceMemberSchema)
def detail(id: int, session: Session = Depends(database_session)):
    handler = AttendanceMemberGetByIdQueryHandler(session)
    query = AttendanceMemberOneQuery(id)
    result = handler.handle(query)
    return result.records


@router.patch("/partial_update/{id}")
def partial_update(id: int, req: AttendanceMemberReq, session: Session = Depends(database_session)):
    signup_dict = req.model_dump(exclude_unset=True)
    handler = AttendanceMemberPartialUpdateCommandHandler(session)
    command = AttendanceMemberPartialUpdateCommand(id)
    command.details = signup_dict
    result = handler.handle(command)

    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/delete/{id}")
def delete(id: int, session: Session = Depends(database_session)):
    handler = AttendanceMemberDeleteCommandHandler(session)
    command = AttendanceMemberDeleteCommand(id)
    result = handler.handle(command)
    if result:
        return JSONResponse(content={'message': 'profile deleted successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'delete profile error'}, status_code=500)