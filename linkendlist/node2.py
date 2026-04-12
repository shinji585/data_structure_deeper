from __future__ import annotations

from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(
        self, data: Optional[T] = None, prev: Optional[Node] = None, next: Optional[Node] = None
    ) -> None:
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next
        self.data = data

    def __repr__(self) -> str:
        prev_data = self.prev.data if self.prev else None
        next_data = self.next.data if self.next else None
        return f"Node(data={self.data}, prev={prev_data}, next={next_data})"
