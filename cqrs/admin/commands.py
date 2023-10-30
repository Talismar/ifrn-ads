

class SignUpCommand:
    def __init__(self):
        self._details: dict[str, any] = dict()

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details):
        self._details = details


class SignUpPartialUpdateCommand:
    def __init__(self, id: int):
        self._details: dict[str, any] = dict()
        self.id = id

    @property
    def details(self):
        return self._details
    
    @details.setter
    def details(self, details) -> bool:
        self._details = details

class SignUpDeleteCommand:
    def __init__(self, id: int):
        self.id = id