from typing import Generic, Optional, TypeVar

from tree.tree_node import Node

T = TypeVar("T")


class BinaryTreeSearch(Generic[T]):
    def __init__(self):
        self.root: Optional[Node[T]] = None

    def find_min(self) -> Node[T]:
        if self.root is None:
            raise ValueError("Tree is empty")

        current: Node[T] = self.root
        while current.left_child is not None:
            current = current.left_child
        return current

    def find_max(self) -> Node[T]:
        if self.root is None:
            raise ValueError("Tree is empty")

        current: Node[T] = self.root
        while current.right_child is not None:
            current = current.right_child
        return current

    def insertion(self, data: T) -> None:
        newNode = Node(data)

        if self.root is None:
            self.root = newNode
        else:
            current: Node[T] = self.root
            parent: Optional[Node[T]] = None
            while True:
                parent = current
                if newNode.data < current.data:
                    assert current.left_child
                    current = current.left_child
                    if current is None:
                        parent.left_child = newNode
                        return
                else:
                    assert current.right_child
                    current = current.right_child
                    if current is None:
                        parent.right_child = newNode
                        return

    def __get_parent_and_node__(self, data: T) -> tuple:
        current: Node[T] = self.root
        parent: Optional[Node[T]] = None

        while current is not None:
            if current.data == data:
                return parent, current

            elif data < current.data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child

        return parent, None
