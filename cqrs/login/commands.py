

class LoginCommand:
    def __init__(self):
        self._details: dict[str, any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details) -> bool:
        self._details = details


class LoginUpdateCommand:
    def __init__(self, id: int):
        self._details: dict[str, any] = dict()
        self.id = id

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details) -> bool:
        self._details = details

class LoginDeleteCommand:
    def __init__(self, id: int):
        self.id = id