# a node is a structure that store a data and the reference to the next value 
from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar('T')

class Node(Generic[T]): 
    """
     this is a node a node is a structure that store a value (data) and the next value (reference) that contain another data 
     and reference
    """
    
    def __init__(self,data: T) -> None:
        self.data: T = data
        self.next: Optional[Node[T]] = None
    
    def __repr__(self):
        return f"Node({self.data},{self.next})"