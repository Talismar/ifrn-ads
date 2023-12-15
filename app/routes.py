from fastapi import APIRouter, HTTPException

from app.database import Database
from app.schemas import ArticheRequestCreateSchema, ArticheSchema

router = APIRouter(prefix="/api")
database = Database()


@router.post("/article", status_code=201)
def article_create(request_data: ArticheRequestCreateSchema):
    request_data_dict = request_data.model_dump()

    artiche_created = database.create_artiches(**request_data_dict)

    return artiche_created


@router.get("/article", response_model=list[ArticheSchema])
def article_list():
    artiches = database.artiches
    return artiches


@router.delete("/article/{id}", status_code=204)
def article_delete(id: int):
    try:
        return database.delete_artiche(id)
    except Exception as exception:
        raise HTTPException(detail=exception.args[0], status_code=404)


@router.get("/article/{id}")
def article_retrieve(id: int):
    try:
        return database.get_by_id(id)
    except Exception as exception:
        raise HTTPException(detail=exception.args[0], status_code=404)
