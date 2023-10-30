from domain.data.sqlalchemy_models import Gym_Class

class GymClassListQuery:
    def __init__(self):
        self._records: list[Gym_Class] = []
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records


class GymClassOneQuery:
    def __init__(self, id):
        self._records: Gym_Class | None = None
        self.id = id
    
    @property
    def records(self):
        return self._records
    
    @records.setter
    def records(self, records):
        self._records = records
