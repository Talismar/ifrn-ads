from .exceptions import HashTableException
from .resource import Resource


class HashTable:
    def __init__(self, size: int):
        self.hash_table: list[Resource | None] = [None for _ in range(size)]
        self.size = size

    def __hash(self, x: int):
        return x % self.size

    def insert(self, resource: Resource) -> None:
        if not isinstance(resource, Resource):
            raise HashTableException(
                f"{resource.__class__.__name__} must be a Resource subclass"
            )

        position = self.__hash(resource.register)

        # Handle collision - finding free position
        if isinstance(self.hash_table[position], Resource):
            initial_position = position
            position = 0 if position + 1 == self.size else position + 1

            while isinstance(self.hash_table[position], Resource):
                if initial_position == position:
                    raise HashTableException("Full __hash table")

                position = 0 if position + 1 == self.size else position + 1

        self.hash_table[position] = resource

    def delete(self, resource_register: int):
        position = self.__get_real_position(resource_register)

        self.hash_table[position] = None

    def search(self, resource_register: int) -> Resource | None:
        position: int = self.__get_real_position(resource_register)
        return self.hash_table[position]

    def __get_real_position(self, resource_register: int):
        position = self.__hash(resource_register)

        # O(1)
        if (
            isinstance(self.hash_table[position], Resource)
            and self.hash_table[position].register == resource_register
        ):
            return position

        # Handle collision - O(n-1)
        else:
            initial_position = position
            position = 0 if position + 1 == self.size else position + 1

            while isinstance(self.hash_table[position], Resource):
                if initial_position == position:
                    raise HashTableException("Resource does not exists")

                if self.hash_table[position].register == resource_register:
                    return position

                position = 0 if position + 1 == self.size else position + 1

        raise HashTableException("Resource does not exists")

    def print_out(self):
        for i in self.hash_table:
            print(i)
