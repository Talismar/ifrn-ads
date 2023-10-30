from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from sqlalchemy.orm import Session
from dependencies import database_session
from domain.request.login import LoginReq, LoginSchema, LoginPartialUpdateReq
from cqrs.login.query.query_handlers import LoginGetAllQueryHandler, LoginGetByIdQueryHandler, LoginOneQuery
from cqrs.login.command.create_handlers import LoginCreateCommandHandler, LoginCommand
from cqrs.login.command.partial_update_handlers import LoginPartialUpdateCommandHandler, LoginUpdateCommand
from cqrs.login.command.delete_handlers import LoginDeleteCommandHandler, LoginDeleteCommand

router = APIRouter(tags=["Login"])

@router.post("/login/add", response_model=LoginReq)
async def add_login(data: LoginReq, session: Session = Depends(database_session)):
    handler = LoginCreateCommandHandler(session)
    command = LoginCommand()
    command.details = data.model_dump()
    result = handler.handle(command)

    if result == True:
        return data
    else:
        return JSONResponse(content={'message': 'create login problem encountered'}, status_code=500)


@router.get("/login/list", response_model=list[LoginSchema])
def list_login(session: Session = Depends(database_session)):
    handler = LoginGetAllQueryHandler(session)
    result = handler.handle()
    return result.records


@router.patch("/login/update/{id}")
async def update_login(id: int, req: LoginPartialUpdateReq, sess: Session = Depends(database_session)):
    login_dict = req.model_dump(exclude_unset=True)
    handler = LoginPartialUpdateCommandHandler(sess)
    command = LoginUpdateCommand(id)
    command.details = login_dict
    result = handler.handle(command)
    if result:
        return JSONResponse(content={'message': 'login updated successfully'}, status_code=201)
    else:
        return JSONResponse(content={'message': 'update login error'}, status_code=500)


@router.delete("/login/delete/{id}")
async def delete_login(id: int, sess: Session = Depends(database_session)):
    handler = LoginDeleteCommandHandler(sess)
    command = LoginDeleteCommand(id)
    result = handler.handle(command)
    if result:
        return JSONResponse(content={'message': 'login deleted successfully'}, status_code=200)
    else:
        return JSONResponse(content={'message': 'delete login error'}, status_code=500)
    

@router.get("/login/get/{id}")
async def get_login(id: int, session: Session = Depends(database_session)) -> LoginSchema:
    handler = LoginGetByIdQueryHandler(session)
    query = LoginOneQuery(id)
    result = handler.handle(query)
    
    if result.records is None:
        return JSONResponse(content={"detail": "Login not found"}, status_code=404)
    
    return result.records
