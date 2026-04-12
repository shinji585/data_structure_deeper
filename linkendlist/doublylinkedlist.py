from typing import Generic, Optional, TypeVar

from node2 import Node

T = TypeVar('T')

class DoublyLinkedList(Generic[T]):
    
    def __init__(self) -> None:
        self.__head: Optional[Node] = None 
        self.__tail: Optional[Node] = None
        self.__size: int = 0
        
    """
     head: point to the first node 
     tail: point to the last node 
     size: is the amount of data store 
    """
    def insert_at_beginning(self,data: T) -> None: 
        newNode = Node(data=data,next=None,prev=None)
        
        if self.__head is None: 
            self.__head = newNode
            self.__tail = newNode
        else: 
            newNode.next = self.__head
            self.__head.prev = newNode
            self.__head = newNode
        
        self.__increase__()
    
    def insert_at_end(self,data: T) -> None: 
        newNode = Node(data=data,next=None,prev=None)
        
        
        if self.__head is None: 
            self.__head = newNode
            self.__tail = newNode
        else:
            assert self.__tail is not None 
            newNode.prev = self.__tail
            self.__tail.next = newNode
            self.__tail = newNode
        
        self.__increase__()
    
    def search(self, data: T) -> bool: 
        for value in self: 
            if value == data:
                return True
        return False
    
    def __increase__(self) -> None: 
        self.__size += 1 
        
    def __decrease__(self) -> None: 
        self.__size -= 1 
        
    def __iter__(self):
        current = self.__head
        while current: 
            yield current.data
            current = current.next
            
    def __len__(self) -> int:
        return self.__size
    
    def __str__(self) -> str:
        return "->".join([str(item) for item in self])
    
    def is_empty(self) -> bool: 
        return self == 0
    
    def clear(self) -> None: 
        self.__head = None 
        self.__tail = None 
        self.__size = 0 