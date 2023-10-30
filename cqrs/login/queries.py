from domain.data.sqlalchemy_models import Login

class LoginListQuery:
    def __init__(self):
        self._records: list[Login] = []
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class LoginOneQuery:
    def __init__(self, id):
        self._records: Login | None = None
        self.id = id
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records
