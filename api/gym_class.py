from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List

from sqlalchemy.orm import Session
from dependencies import database_session
from domain.request.gym_class import GymClassReq, GymClassSchema
from cqrs.gym_class.command.create_handlers import (
    GymClassCreateCommandHandler, 
    GymClassCommand
)
from cqrs.gym_class.command.partial_update_handlers import (
    GymClassPartialUpdateCommandHandler, 
    GymClassPartialUpdateCommand
)
from cqrs.gym_class.command.delete_handlers import (
    GymClassDeleteCommandHandler, 
    GymClassDeleteCommand
)
from cqrs.gym_class.query.query_handlers import (
    GymClassGetAllQueryHandler,
    GymClassGetByIdQueryHandler,
    GymClassOneQuery
)

router = APIRouter(prefix="/gym_class", tags=["Gym Class"])

@router.post("/create")
def create(data: GymClassReq, session: Session = Depends(database_session)):
    handler = GymClassCreateCommandHandler(session)
    command = GymClassCommand()
    command.details = data.model_dump()
    result = handler.handle(command)
    if result == True:
        return data
    else:
        return JSONResponse(content={'message': 'create signup problem encountered'}, status_code=500)


@router.get("/list", response_model=List[GymClassSchema])
def list(session: Session = Depends(database_session)):
    handler = GymClassGetAllQueryHandler(session)
    result = handler.handle()
    return result.records


@router.get("/detail/{id}", response_model=GymClassSchema)
def detail(id: int, session: Session = Depends(database_session)):
    handler = GymClassGetByIdQueryHandler(session)
    query = GymClassOneQuery(id)
    result = handler.handle(query)
    return result.records


@router.patch("/partial_update/{id}")
def partial_update(id: int, req: GymClassReq, session: Session = Depends(database_session)):
    signup_dict = req.model_dump(exclude_unset=True)
    handler = GymClassPartialUpdateCommandHandler(session)
    command = GymClassPartialUpdateCommand(id)
    command.details = signup_dict
    result = handler.handle(command)

    if result:
        return JSONResponse(content={'message': 'profile updated successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'update profile error'}, status_code=500)


@router.delete("/delete/{id}")
def delete(id: int, session: Session = Depends(database_session)):
    handler = GymClassDeleteCommandHandler(session)
    command = GymClassDeleteCommand(id)
    result = handler.handle(command)
    if result:
        return JSONResponse(content={'message': 'profile deleted successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'delete profile error'}, status_code=500)