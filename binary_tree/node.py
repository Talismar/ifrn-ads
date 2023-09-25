class Node:
    def __init__(self, data: int) -> None:
        self._data = data
        self.left: Node | None = None
        self.right: Node | None = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data: int):
        self._data = new_data
