from fastapi import FastAPI, Depends
from .configs.local import settings
from app.http.routes import app_routes
from app.http.middleware import HTTPRequestAuditMiddleware

app = FastAPI()

app.add_middleware(HTTPRequestAuditMiddleware)

for route in app_routes:
    app.include_router(route)
