# a single linkend list is not a list as the you could think, the best definition for this is a only node that has the function 
# of be a point to the start and that goint from it to the end 


from typing import Generator, Generic, Optional, TypeVar

from node import Node

T = TypeVar('T')

class SinglyLinkedList(Generic[T]):
    """
     the singly linked list class only contains two attribute: the size, and the head 
    """
    def __init__(self) -> None:
        self.__head: Optional[Node] = None
        self.__size = 0 
        
        
    # dunder methods 
    def __len__(self):
        return self.__size
    
    def __iter__(self) -> Generator:
        current = self.__head
        while current: 
            yield current.data
            current = current.next
        
    def append(self,data: T) -> None: 
        newNode = Node(data=data)
        
        if self.__head is None: 
            self.__head = newNode
        else: 
            current = self.__head
            while current.next is not None: 
                current = current.next
            current.next = newNode
        
        self.__size += 1 
    