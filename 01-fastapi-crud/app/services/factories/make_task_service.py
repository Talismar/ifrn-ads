from fastapi import Depends
from ..task import TaskService
from app.repositories.sqlalchemy import SqlalchemyTaskRepository

from app.dependencies import get_db_connection


def make_task_service(session=Depends(get_db_connection)):
    task_repository = SqlalchemyTaskRepository(session)
    return TaskService(task_repository)
