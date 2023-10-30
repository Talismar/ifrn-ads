from domain.data.sqlalchemy_models import Profile_Members

class ProfileMembersListQuery:
    def __init__(self):
        self._records: list[Profile_Members] = []
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class ProfileMembersOneQuery:
    def __init__(self, id):
        self._records: Profile_Members | None = None
        self.id = id
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records
