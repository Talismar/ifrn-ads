from pydantic import BaseModel
from datetime import date

class LoginBase(BaseModel): 
    username: str 
    date_approved:date
    user_type:int

class LoginReq(LoginBase): 
    password: str 


class LoginPartialUpdateReq(BaseModel): 
    password: str | None = None
    username: str | None = None
    date_approved:date | None = None
    user_type:int | None = None

class LoginSchema(LoginBase): 
    id: int