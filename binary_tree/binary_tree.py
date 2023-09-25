from .exceptions import BinaryTreeException
from .node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        self.__root: Node | None = None

    @property
    def root(self) -> Node | None:
        return self.__root

    def insert(self, data: int):
        if self.__root is None:
            self.__root = Node(data)
        else:
            temp = self.__root
            while True:
                if data < temp.data:
                    if temp.left is None:
                        temp.left = Node(data)
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Node(data)
                        break
                    else:
                        temp = temp.right

    def count_nodes(self, no: Node | None):
        if no is None:
            return 0

        if no.left is None and no.right is None:
            return 1

        return self.count_nodes(no.left) + self.count_nodes(no.right)

    def search(self, data):
        if self.__root is None:
            return None
        else:
            temp = self.__root
            while temp is not None:
                if data == temp.data:
                    return data

                elif data < temp.data:
                    temp = temp.left
                else:
                    temp = temp.right
            return "Not found"

    def find_minor(self):
        if self.is_empty():
            BinaryTreeException()

        temp = self.__root

        while temp.left is not None:
            temp = temp.left

        return temp.data

    def find_greater(self):
        if self.is_empty():
            BinaryTreeException()

        temp = self.__root

        while temp.right is not None:
            temp = temp.right

        return temp.data

    def is_empty(self):
        return self.__root is None

    def print_out_in_order(self, aux: Node | None):
        if aux is not None:
            self.print_out_in_order(aux.left)
            print(aux.data, end=" ")
            self.print_out_in_order(aux.right)

    def __repr__(self) -> str:
        aux = self.__root
        self.print_out_in_order(aux)
        return ""
