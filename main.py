from hash_table import HashTable, Resource


class Student(Resource):
    def __init__(self, name: str, register: int) -> None:
        super().__init__(register)
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name} - {self.register}"


hash_instance: HashTable = HashTable(10)
student1 = Student("Talismar 1", 12345)
student2 = Student("Talismar 2", 12346)
student3 = Student("Talismar 3", 12347)
hash_instance.insert(student1)
hash_instance.insert(student2)
hash_instance.insert(student3)

hash_instance.delete(12345)
hash_instance.print_out()

print(">>> ", hash_instance.search(12347))
