from domain.data.sqlalchemy_models import Profile_Trainers

class AttendanceMemberListQuery:
    def __init__(self):
        self._records: list[Profile_Trainers] = []
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class AttendanceMemberOneQuery:
    def __init__(self, id):
        self._records: Profile_Trainers | None = None
        self.id = id
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records
