from fastapi import FastAPI
from api import api_routes


app = FastAPI()

for route in api_routes:
    app.include_router(route)
