from app.repositories.task_repository import TaskRepository
from fastapi import HTTPException, Response
from sqlalchemy.exc import IntegrityError


class TaskService:
    def __init__(self, task_repository: TaskRepository) -> None:
        self.task_repository = task_repository

    def list_all(self):
        return self.task_repository.list_all()

    def create(self, data, created_by):
        try:
            return self.task_repository.create(data, created_by)
        except IntegrityError as error:
            raise HTTPException(status_code=400, detail="Error creating task")

    def delete(self, id):
        try:
            self.task_repository.delete(id)
            return Response(status_code=204)
        except:
            raise HTTPException(status_code=400, detail="Error deleting task")

    def get_one(self, id):
        obj = self.task_repository.get_by_id(id)

        if obj is None:
            raise HTTPException(status_code=400, detail="Error getting task")
        return obj

    def partial_update(self, id, data):
        return self.task_repository.partial_update(id, data)
