from pydantic import BaseModel


class ArticheRequestCreateSchema(BaseModel):
    title: str
    content: str


class ArticheSchema(ArticheRequestCreateSchema):
    id: int
