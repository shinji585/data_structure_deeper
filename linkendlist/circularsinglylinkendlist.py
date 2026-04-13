from typing import Generator, Generic, Optional, TypeVar

from .node import Node

T = TypeVar('T')

class CircularSynglyLinkedList(Generic[T]): 
    
    def __init__(self) -> None:
        self.__head: Optional[Node] = None
        self.__tail: Optional[Node] = None 
        self.__size: int = 0 
        
    def append(self,data: T) -> None: 
        newNode = Node(data=data)
        
        if self.__head is None: 
            newNode.next = newNode
            self.__head = newNode
            self.__tail = newNode
        else: 
            assert self.__tail is not None
            self.__tail.next = newNode
            newNode.next = self.__head
            self.__tail = newNode
        
        self.__inscrease__()
        
    def delete(self,reference: T) -> None: 
        current = self.__head
        prev = self.__tail
        
        if current is None: 
            return
        
        while True: 
            assert current is not None
            if current.data == reference: 
                
                # caso 1: 
                if self.__size == 1: 
                    self.__head = None
                    self.__tail = None 
                    self.__decrease__()
                    return
                    
                # case 2: 
                elif current == self.__head: 
                    self.__head = current.next
                    assert self.__tail is not None 
                    self.__tail.next = self.__head
                    
                # case 3: 
                elif current == self.__tail: 
                    self.__tail = prev
                    assert self.__tail is not None
                    self.__tail.next = self.__head
                    
                else:
                    assert prev is not None
                    prev.next = current.next
                    
                self.__decrease__()
                return
            prev = current
            current = current.next
            
            if current == self.__head: 
                break
                    
    def __inscrease__(self) -> None: 
        self.__size += 1 
    
    def __decrease__(self) -> None: 
        self.__size -= 1 
        
    def __clear__(self): 
        self.__head = None 
        self.__tail = None
        self.__size = 0 
        
    def __iter__(self) -> Generator:
        
        if self.__head is None: 
            return
        
        current = self.__head
        while True:
            yield current.data # type: ignore
            current = current.next # type: ignore 
            if current == self.__head:
                break