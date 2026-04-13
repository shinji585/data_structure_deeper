from typing import Generator, Generic, Optional, TypeVar

from .node2 import Node

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
        
    def insert_before(self,data: T, reference: T) -> None: 
        if self.__head is None: 
            return
        
        if self.__head.data == reference: 
            self.insert_at_beginning(data=data)
            return
        
        current: Optional[Node] = self.__head
        while current is not None and current.data != reference: 
            current = current.next
            
        if current is None: 
            return
        
        newNode = Node(data=data, next=None, prev=None)
        newNode.next = current
        newNode.prev = current.prev
        
        if current.prev is not None: 
            current.prev.next = newNode
            
        current.prev = newNode
        self.__increase__()
            
    def insert_after(self,data: T, reference: T) -> None: 
        current = self.__head  
        
        while current is not None and current.data != reference: 
            current = current.next
            
        if current is None: 
            return
        
        newNode = Node(data=data, next=None, prev=None)
        newNode.next = current.next
        newNode.prev = current
        
        if current.next is not None: 
            current.next.prev = newNode
            
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
            assert self.__head is not None
            self.__head.prev = None   
            
        self.__decrease__() 
        
    def remove_at_end(self) -> None: 
        if self.__head is None: 
            return
        
        if self.__head == self.__tail: 
            self.__head = None
            self.__tail = None 
        else: 
            assert self.__tail is not None
            self.__tail = self.__tail.prev  
            
            assert self.__tail is not None
            self.__tail.next = None   
            
        self.__decrease__()
        
    def remove(self,reference: T) -> None: 
        if self.__head is None: 
            return
         
        current: Optional[Node] = self.__head
        while current is not None and current.data != reference:
            current = current.next
                
        if current is None: 
            return    

        if current == self.__head: 
            self.remove_at_beginning()
            return
            
        if current == self.__tail: 
            self.remove_at_end()
            return
        
        assert current.prev is not None 
        current.prev.next = current.next
        
        assert current.next is not None
        current.next.prev = current.prev
            
        self.__decrease__()
    
    
    def search(self, data: T) -> bool: 
        for value in self: 
            if value == data:
                return True
        return False
    
    def __increase__(self) -> None: 
        self.__size += 1 
        
    def __decrease__(self) -> None: 
        self.__size -= 1 
        
    def __iter__(self) -> Generator:
        current = self.__head
        while current: 
            yield current.data
            current = current.next
            
    def __len__(self) -> int:
        return self.__size
    
    def __str__(self) -> str:
        return "->".join([str(item) for item in self])
    
    def is_empty(self) -> bool: 
        return len(self) == 0
    
    def clear(self) -> None: 
        self.__head = None 
        self.__tail = None 
        self.__size = 0

    @property
    def head(self) -> Optional[Node[T]]:
        return self.__head

    @property
    def tail(self) -> Optional[Node[T]]:
        return self.__tail

    @property
    def size(self) -> int:
        return self.__size 