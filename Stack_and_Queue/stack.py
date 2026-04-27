from typing import Generic, Optional, TypeVar

from linkendlist.node import Node

T = TypeVar('T')

class Stack(Generic[T]):
    
    def __init__(self) -> None:
        self.__top: Optional[Node[T]] = None
        self.__size: int = 0 
        
    def push(self,x: T) -> None: 
        newTop = Node(data=x)
        
        if self.__top: 
            newTop.next = self.__top
            self.__top = newTop
        else: 
            self.__top = newTop
            
        self.__increase__()
    
    def pop(self) -> Optional[T]: 
            if self.__top: 
                data = self.__top.data
                self.__decrease__()
                if self.__top.next: 
                    self.__top = self.__top.next
                return data
            else: 
                return None
    
    def peek(self) -> Optional[T]: 
        if self.__top: 
            return self.__top.data
        else: 
            return None

        
    def __increase__(self) -> None: 
        self.__size += 1 
        
    def __decrease__(self) -> None: 
        self.__size -= 1 
        
    def is_empty(self) -> bool: 
        return self.__top is None
    
    def __iter__(self):
        current = self.__top
        while current: 
            yield current.data
            current = current.next