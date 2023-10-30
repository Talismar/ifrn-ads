from domain.data.sqlalchemy_models import Signup, Profile_Members, Attendance_Member

class SignUpListQuery:
    def __init__(self):
        self._records: list[Signup] = []
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class SignUpOneQuery:
    def __init__(self, id):
        self._records: Signup | None = None
        self.id = id
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class LoginMemberJoinQuery:
    def __init__(self):
        self._records: list[Profile_Members] = []
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class AttendanceMemberJoinQuery:
    def __init__(self):
        self._records: list[Attendance_Member] = []
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records