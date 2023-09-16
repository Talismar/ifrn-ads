from fastapi import FastAPI, Depends
from .configs.local import settings
from app.http.routes import app_routes

app = FastAPI()

for route in app_routes:
    app.include_router(route)
