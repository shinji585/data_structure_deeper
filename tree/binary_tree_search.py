from typing import TypeVar, Generic, Optional
from tree.tree_node import Node

T = TypeVar("T")


class BinaryTreeSearch(Generic[T]):
    def __init__(self):
        self.root: Optional[Node] = None

    def find_min(self) -> Node[T]:
        if self.root is None:
            raise ValueError("Node is empty")

        current = self.root
        while current.left_child is not None:
            current = current.left_child
        return current

    def find_max(self) -> Node[T]:
        if self.root is None:
            raise ValueError("Node is empty")

        current = self.root
        while current.right_child is not None:
            current = current.right_child
        return current
