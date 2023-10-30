from typing import List
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from dependencies import database_session
from domain.request.trainers import ProfileTrainersReq
from cqrs.profile_trainers.command.create_handlers import (
    ProfileTrainersCreateCommandHandler, 
    ProfileTrainersCommand
)
from cqrs.profile_trainers.command.partial_update_handlers import (
    ProfileTrainersPartialUpdateCommandHandler, 
    ProfileTrainersPartialUpdateCommand
)
from cqrs.profile_trainers.command.delete_handlers import (
    ProfileTrainersDeleteCommandHandler, 
    ProfileTrainersDeleteCommand
)
from cqrs.profile_trainers.query.query_handlers import (
    ProfileTrainersGetAllQueryHandler,
    ProfileTrainersGetByIdQueryHandler,
    ProfileTrainersOneQuery
)

router = APIRouter(prefix="/profile_trainers", tags=["Profile Trainers"])

@router.post("/create")
def create(data: ProfileTrainersReq, session: Session = Depends(database_session)):
    handler = ProfileTrainersCreateCommandHandler(session)
    command = ProfileTrainersCommand()
    command.details = data.model_dump()
    result = handler.handle(command)

    if result == True:
        return JSONResponse(content=jsonable_encoder(data), status_code=201)
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)


@router.get("/list", response_model=List[ProfileTrainersReq])
def list(session: Session = Depends(database_session)):
    handler = ProfileTrainersGetAllQueryHandler(session)
    result = handler.handle()
    return result.records


@router.get("/detail/{id}", response_model=ProfileTrainersReq)
def detail(id: int, session: Session = Depends(database_session)):
    handler = ProfileTrainersGetByIdQueryHandler(session)
    query = ProfileTrainersOneQuery(id)
    result = handler.handle(query)
    return result.records


@router.patch("/partial_update/{id}")
def partial_update(id: int, req: ProfileTrainersReq, session: Session = Depends(database_session)):
    signup_dict = req.model_dump(exclude_unset=True)
    handler = ProfileTrainersPartialUpdateCommandHandler(session)
    command = ProfileTrainersPartialUpdateCommand(id)
    command.details = signup_dict
    result = handler.handle(command)

    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/delete/{id}")
def delete(id: int, session: Session = Depends(database_session)):
    handler = ProfileTrainersDeleteCommandHandler(session)
    command = ProfileTrainersDeleteCommand(id)
    result = handler.handle(command)
    if result:
        return JSONResponse(content={'message': 'profile deleted successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'delete profile error'}, status_code=500)