from .login import router as login_router
from .admin import router as admin_router
from .profile_members import router as profile_members_router
from .profile_trainers import router as profile_trainers_router
from .gym_class import router as gym_class_router
from .attendance_member import router as attendance_member_router

api_routes = [
    login_router, 
    admin_router, 
    profile_members_router, 
    profile_trainers_router, 
    gym_class_router,
    attendance_member_router
]