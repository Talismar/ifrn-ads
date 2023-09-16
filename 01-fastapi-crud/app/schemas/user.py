from datetime import datetime
from fastapi import Form, UploadFile, File
from typing import Union, Optional
from pydantic import BaseModel, EmailStr, Field, HttpUrl


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr


class UserSchema(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class UserPostRequestSchema(UserBaseSchema):
    password: str = Field(
        description="Password of the user", min_length=6, max_length=8
    )
    password_confirm: str = Field(
        description="Confirm password", min_length=6, max_length=8
    )


class UserLoginPostRequestSchema(BaseModel):
    password: str = Field(
        description="Password of the user", min_length=6, max_length=8
    )
    email: EmailStr


class UserPartialUpdateRequestSchema(BaseModel):
    name: Optional[str] = None


class UserPartialUpdateParams:
    def __init__(
        self,
        name: Union[str, None] = Form(None),
    ):
        self.name = name
