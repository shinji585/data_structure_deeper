from typing import Generator, Generic, Optional, TypeVar

from node import Node

T = TypeVar('T')

class SinglyLinkedList(Generic[T]):
    
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
        newNode = Node(data=data)
        
        if self.__head is None:
            """
            CASE 1: in this case both point to newNode because is the first node store 
            """
            self.__head = newNode
            self.__tail = newNode
        else: 
            """
            CASE 2: In this case head connect the last value before to the new and then move to it 
            """
            newNode.next = self.__head
            self.__head = newNode 
            
        self.__increase__()
        
    
    def insert_at_end(self,data: T) -> None: 
        newNode = Node(data=data)
        
        if self.__tail is None:  
            """
            CASE 1: in this case both point to newNode because is the first node store 
            """
            self.__head = newNode
            self.__tail = newNode
        else: 
            """
            CASE 2: In this case tail connect the last value before to the new and then move to it 
            """
            self.__tail.next = newNode
            self.__tail = newNode
            
        self.__increase__()
        
    def insert_before(self,data: T,reference: T) -> None: 
        if self.__head is None: 
            return 
        
        if self.__head.data == reference: 
            self.insert_at_beginning(data=data)
            return 
        
        prev: Optional[Node] = None 
        current: Optional[Node] = self.__head
        
        while current is not None and current.data != reference: 
            prev = current
            current = current.next
            
        if current is not None and current.data == reference: 
            newNode = Node(data=data)
            assert prev is not None
            prev.next = newNode
            newNode.next = current
            self.__increase__()
            
    def insert_after(self,data: T,reference: T) -> None:         
        current = self.__head

        while current is not None and current.data != reference: 
            current = current.next
            
        if current is not None and current.data == reference: 
            newNode = Node(data=data)
            newNode.next = current.next
            current.next = newNode 
            
            if current == self.__tail:
                self.__tail = newNode
                
            self.__increase__()
                                          
     
    def remove_at_beginning(self) -> None:
        if self.__head is None: 
            return 
        
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
        self.__decrease__()
        
    def remove_at_end(self) -> None: 
        if self.__head is None: 
            return
        
        if self.__head == self.__tail: 
            self.__head = None
            self.__tail = None 
        else: 
            prev: Optional[Node] = None 
            current = self.__head
            while current.next is not None: 
                prev = current
                current = current.next
                
            assert prev is not None
            prev.next = None 
            self.__tail = prev
        self.__decrease__()
            
    def remove(self,reference: T) -> None: 
        if self.__head is None: 
            return
        
        if self.__head.data == reference:
            self.remove_at_beginning()
            return
        
        prev: Optional[Node] = None 
        current: Optional[Node] = self.__head
        while current is not None and current.data != reference:
            prev =  current 
            current = current.next
                
        if current is None: 
            return    
            
        assert prev is not None
        if current == self.__tail: 
            prev.next = None
            self.__tail = prev
        else:
            prev.next = current.next
            
        self.__decrease__()
                
    def clear(self) -> None: 
        self.__head = None 
        self.__tail = None
        self.__size = 0 
        
    def search(self,reference: T) -> bool: 
        for value in self: 
            if value == reference: 
                return True
        return False          
                
    def __len__(self) -> int:
        return self.__size
    
    def __iter__(self) -> Generator:
        current = self.__head
        while current: 
            yield current.data
            current = current.next
            
    def is_empty(self) -> bool: 
        return self == 0
            
    def __increase__(self) -> None: 
        self.__size += 1  
        
    def __decrease__(self) -> None: 
        self.__size -= 1 