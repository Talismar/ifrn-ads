from fastapi import APIRouter, Depends
from ..controllers import task
from app.schemas.task import TaskSchema
from app.http.dependencies.current_user_dependency import CurrentUserDependency


current_user_dependency = CurrentUserDependency()

router = APIRouter(
    prefix="/task", tags=["task"], dependencies=[Depends(current_user_dependency)]
)

router.add_api_route(
    "/", task.create, methods=["POST"], status_code=201, response_model=TaskSchema
)
router.add_api_route(
    "/", task.list_all, methods=["GET"], response_model=list[TaskSchema]
)
router.add_api_route(
    "/{task_id}", task.get_one, methods=["GET"], response_model=TaskSchema
)
router.add_api_route(
    "/{task_id}", task.delete, methods=["DELETE"], status_code=204, response_model=None
)
router.add_api_route(
    "/{task_id}", task.partial_update, methods=["PATCH"], response_model=TaskSchema
)
