from __future__ import annotations

from typing import TypeVar, Generic, Optional

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.left_child: Optional[Node[T]] = None
        self.right_child: Optional[Node[T]] = None
