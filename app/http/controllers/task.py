from app.services.factories.make_task_service import make_task_service
from fastapi import Depends, Request
from app.services.task import TaskService
from app.schemas.task import TaskPostRequestSchema, TaskPartialUpdateRequestSchema


def list_all(task_service: TaskService = Depends(make_task_service)):
    return task_service.list_all()


def get_one(task_id: int, task_service: TaskService = Depends(make_task_service)):
    return task_service.get_one(task_id)


def create(
    request: Request,
    data: TaskPostRequestSchema,
    task_service: TaskService = Depends(make_task_service),
):
    return task_service.create(data, request.user)


def delete(task_id: int, task_service: TaskService = Depends(make_task_service)):
    return task_service.delete(task_id)


def partial_update(
    task_id: int,
    data: TaskPartialUpdateRequestSchema,
    task_service: TaskService = Depends(make_task_service),
):
    return task_service.partial_update(task_id, data)
