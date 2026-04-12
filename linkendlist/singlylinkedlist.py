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
        self.__tail: Optional[Node] = None
        self.__size = 0 
        
        
    # dunder methods 
    def __len__(self):
        return self.__size
    
    def __iter__(self) -> Generator:
        current = self.__tail
        while current: 
            yield current.data
            current = current.next
            
    def __str__(self) -> str:
        return f"Values({[x for x in self.__iter__()]})"
            
            
    # operations of the interface
    
        
    def append(self,data: T) -> None: 
        newNode = Node(data=data)
        
        if self.__head is None: 
            self.__head = newNode
            self.__tail = newNode
        else: 
            self.__head.next = newNode
            self.__head = newNode
        
        self.__size += 1
        
        
    def remove(self, data: T) -> None: 
        current = self.__tail
        prev: Optional[Node] = None
        while current: 
            if current.data == data:
                if prev is None: 
                    self.__tail = current.next
                else: 
                    prev.next = current.next
                
                if current == self.__head: 
                    self.__head = prev
                    
                self.__size -= 1 
                return 
            
            prev = current
            current = current.next
            
    def search(self,data: T) -> bool: 
        for node in self.__iter__():
            if data == node: 
                return True
        return False
                
    def clear(self): 
        """ clear the entire list. """
        self.__tail = None
        self.__head = None
            