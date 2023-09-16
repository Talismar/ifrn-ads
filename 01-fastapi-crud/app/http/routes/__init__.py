from .user import router as user_router
from .task import router as task_router
from .authentication import router as authentication_router

app_routes = [user_router, task_router, authentication_router]
