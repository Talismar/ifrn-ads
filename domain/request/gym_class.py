from pydantic import BaseModel, validator

class GymClassReq(BaseModel): 
    member_id: int
    trainer_id: int
    approved_id: int
    name: str
    
class GymClassSchema(GymClassReq):
    id: int