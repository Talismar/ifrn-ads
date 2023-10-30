from pydantic import BaseModel


class SignupBase(BaseModel):  
    username: str 
        
    class Config:
        from_attributes = True

class SignupReq(SignupBase):
    password: str 


class SignupSchema(SignupBase):
    id : int