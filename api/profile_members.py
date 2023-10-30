from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from dependencies import database_session
from domain.request.members import ProfileMembersReq
from cqrs.profile_members.command.create_handlers import (
    ProfileMembersCreateCommandHandler, 
    ProfileMembersCommand
)
from cqrs.profile_members.command.partial_update_handlers import (
    ProfileMembersPartialUpdateCommandHandler, 
    ProfileMembersPartialUpdateCommand
)
from cqrs.profile_members.command.delete_handlers import (
    ProfileMembersDeleteCommandHandler, 
    ProfileMembersDeleteCommand
)
from cqrs.profile_members.query.query_handlers import (
    ProfileMembersGetAllQueryHandler,
    ProfileMembersGetByIdQueryHandler,
    ProfileMembersOneQuery
)

router = APIRouter(prefix="/profile_members", tags=["Profile Members"])

@router.post("/create")
def create(data: ProfileMembersReq, session: Session = Depends(database_session)):
    handler = ProfileMembersCreateCommandHandler(session)
    command = ProfileMembersCommand()
    command.details = data.model_dump()
    print("HERE")
    result = handler.handle(command)
    if result == True:
        return data
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)


@router.get("/list", response_model=List[ProfileMembersReq])
def list(session: Session = Depends(database_session)):
    handler = ProfileMembersGetAllQueryHandler(session)
    result = handler.handle()
    return result.records


@router.get("/detail/{id}", response_model=ProfileMembersReq)
def detail(id: int, session: Session = Depends(database_session)):
    handler = ProfileMembersGetByIdQueryHandler(session)
    query = ProfileMembersOneQuery(id)
    result = handler.handle(query)
    return result.records


@router.patch("/partial_update/{id}")
def partial_update(id: int, req: ProfileMembersReq, session: Session = Depends(database_session)):
    signup_dict = req.model_dump(exclude_unset=True)
    handler = ProfileMembersPartialUpdateCommandHandler(session)
    command = ProfileMembersPartialUpdateCommand(id)
    command.details = signup_dict
    result = handler.handle(command)
    
    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/delete/{id}")
def delete(id: int, session: Session = Depends(database_session)):
    handler = ProfileMembersDeleteCommandHandler(session)
    command = ProfileMembersDeleteCommand(id)
    result = handler.handle(command)
    if result:
        return JSONResponse(content={'message': 'profile deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete profile error'}, status_code=500)