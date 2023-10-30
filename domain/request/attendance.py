from pydantic import BaseModel
from datetime import date, time





class AttendanceMemberReq(BaseModel):
    member_id: int
    timeout: time
    timein: time
    date_log: date

class AttendanceMemberSchema(AttendanceMemberReq):
    id: int