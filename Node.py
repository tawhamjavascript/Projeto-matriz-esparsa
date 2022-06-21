class Node:
    def __init__(self, value):
        self.__value = value
        self.__left = None
        self.__right = None
        self.__height = 1

    def get_left(self) -> "Node":
        return self.__left

    def set_left(self, value) -> None:
        self.__left = value

    def get_right(self) -> "Node":
        return self.__right

    def set_right(self, value) -> None:
        self.__right = value

    def get_height(self) -> int:
        return self.__height

    def set_height(self, new_height) -> None:
        self.__height = new_height

    def get_value(self):
        return self.__value

    def set_value(self, value) -> None:
        self.__value = value

    def __str__(self):
        return f"| {self.__value}: h = {self.__height}"

