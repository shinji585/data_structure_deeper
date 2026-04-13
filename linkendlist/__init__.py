"""
LinkEndList - Linked List implementations

This package contains implementations of various linked list structures:
- SinglyLinkedList: Single direction linked list
- DoublyLinkedList: Bidirectional linked list
"""

from .doublylinkedlist import DoublyLinkedList
from .node import Node as SingleNode
from .node2 import Node as DoubleNode
from .singlylinkedlist import SinglyLinkedList

__all__ = [
    "SinglyLinkedList",
    "DoublyLinkedList",
    "SingleNode",
    "DoubleNode",
]
