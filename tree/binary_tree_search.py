from typing import Any, Optional, Protocol, Iterator

from tree.tree_node import Node


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...


class BinaryTreeSearch[T: Comparable]:
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

    def insert(self, data: T) -> None:
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

    def remove(self, data: T) -> bool:
        parent, node = self.__get_parent_and_node__(data)

        if parent is None and node is None:
            return False

        # children count
        children_count: int = 0

        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1

        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                self.root = None
        elif children_count == 1:
            next_node: Optional[Node[T]] = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node: Node[T] = node.right_child
            while leftmost_node.left_child is not None:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node.data

            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
        return True

    def search(self, data: T) -> bool:
        current: Optional[Node[T]] = self.root

        while current is not None:
            if current.data == data:
                return True

            if data < current.data:
                current = current.left_child
            else:
                current = current.right_child

        return False

    def preorder(self) -> None:
        self.__preorder__(self.root)

    def inorder(self) -> None:
        self.__inorder__(self.root)

    def postorder(self) -> None:
        self.__postorder__(self.root)

    def __get_parent_and_node__(self, data: T) -> tuple:
        current: Optional[Node[T]] = self.root
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

    def __preorder__(self, current: Optional[Node[T]]) -> Iterator[T]:

        if current is None:
            return

        yield current.data

        yield from self.__preorder__(current.left_child)
        yield from self.__preorder__(current.right_child)

    def __inorder__(self, current: Optional[Node[T]]) -> Iterator[T]:

        if current is None:
            return

        yield from self.__inorder__(current.left_child)
        yield current.data
        yield from self.__inorder__(current.right_child)

    def __postorder__(self, current: Optional[Node[T]]) -> Iterator[T]:

        if current is None:
            return

        yield from self.__postorder__(current.left_child)
        yield from self.__postorder__(current.right_child)
        yield current.data
