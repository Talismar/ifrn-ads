from app.schemas.task import TaskPostRequestSchema
from sqlalchemy.orm import Session
from app.models import Task
from app.repositories.task_repository import TaskRepository


class SqlalchemyTaskRepository(TaskRepository[Session]):
    def list_all(self):
        return self._db.query(Task).all()

    def create(self, task: TaskPostRequestSchema, created_by):
        db_task = Task(created_by_id=created_by.id, **task.model_dump())

        self._db.add(db_task)
        self._db.commit()
        self._db.refresh(db_task)

        return db_task

    def get_by_id(self, id: int):
        return self._db.query(Task).filter_by(id=id).first()

    def get_by_email(self, email: str):
        return self._db.query(Task).filter_by(email=email).first()

    def partial_update(self, id: int, data):
        db_task = self._db.query(Task).filter_by(id=id).first()

        for field, value in data.model_dump().items():
            if value is not None:
                setattr(db_task, field, value)

        self._db.commit()
        return db_task

    def delete(self, id):
        obj = self._db.get(Task, id)
        self._db.delete(obj)
        self._db.commit()
