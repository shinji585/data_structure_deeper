from typing import  Generic, TypeVar

T = TypeVar('T')

class ListQueue(Generic[T]):

    def __init__(self) -> None:
        self.item__: list[T] = []
        self.__size = 0

    def enqueue(self,data: T) -> None:
        self.item__.insert(0,data)
        self.__size += 1

    def dequeue(self) -> T:
        data = self.item__.pop()
        self.__size -= 1
        return data

    def __len__(self) -> int:
        return  self.__size

    @property
    def items(self) -> list[T]:
        return  self.item__