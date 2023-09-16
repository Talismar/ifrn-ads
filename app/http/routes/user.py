from fastapi import APIRouter, Depends
from ..controllers import user
from app.schemas.user import UserSchema
from app.http.dependencies.current_user_dependency import CurrentUserDependency


current_user_dependency = CurrentUserDependency()

router = APIRouter(prefix="/user", tags=["user"])

router.add_api_route(
    "/", user.create, methods=["POST"], status_code=201, response_model=UserSchema
)
router.add_api_route(
    "/",
    user.list_all,
    methods=["GET"],
    response_model=list[UserSchema],
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/{user_id}",
    user.get_one,
    methods=["GET"],
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/{user_id}",
    user.delete,
    methods=["DELETE"],
    status_code=204,
    dependencies=[Depends(current_user_dependency)],
)
router.add_api_route(
    "/{user_id}",
    user.partial_update,
    methods=["PATCH"],
    response_model=UserSchema,
    dependencies=[Depends(current_user_dependency)],
)
