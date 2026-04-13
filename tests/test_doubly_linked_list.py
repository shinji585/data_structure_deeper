"""
Test suite for DoublyLinkedList implementation
"""

from linkendlist.doublylinkedlist import DoublyLinkedList


class TestDoublyLinkedList:
    """Tests for DoublyLinkedList implementation"""

    def setup_method(self):
        """Setup method to initialize a fresh list before each test"""
        self.dll: DoublyLinkedList[int] = DoublyLinkedList()

    def test_insert_at_beginning_empty_list(self):
        """Test inserting at beginning in an empty list"""
        self.dll.insert_at_beginning(10)
        head = self.dll.head
        tail = self.dll.tail
        assert head is not None
        assert head.data == 10
        assert tail is not None
        assert tail.data == 10
        assert self.dll.size == 1

    def test_insert_at_beginning_multiple(self):
        """Test inserting multiple elements at beginning"""
        self.dll.insert_at_beginning(1)
        self.dll.insert_at_beginning(2)
        self.dll.insert_at_beginning(3)
        head = self.dll.head
        tail = self.dll.tail
        assert head is not None
        assert head.data == 3
        assert tail is not None
        assert tail.data == 1
        assert self.dll.size == 3

    def test_insert_at_beginning_prev_reference(self):
        """Test that prev reference is None at head"""
        self.dll.insert_at_beginning(1)
        self.dll.insert_at_beginning(2)
        head = self.dll.head
        assert head is not None
        assert head.prev is None

    def test_insert_at_end_empty_list(self):
        """Test inserting at end in an empty list"""
        self.dll.insert_at_end(10)
        head = self.dll.head
        tail = self.dll.tail
        assert head is not None
        assert head.data == 10
        assert tail is not None
        assert tail.data == 10
        assert self.dll.size == 1

    def test_insert_at_end_multiple(self):
        """Test inserting multiple elements at end"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        head = self.dll.head
        tail = self.dll.tail
        assert head is not None
        assert head.data == 1
        assert tail is not None
        assert tail.data == 3
        assert self.dll.size == 3

    def test_insert_at_end_next_reference(self):
        """Test that next reference is None at tail"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        tail = self.dll.tail
        assert tail is not None
        assert tail.next is None

    def test_insert_before_at_head(self):
        """Test inserting before the head"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_before(0, 1)
        head = self.dll.head
        assert head is not None
        assert head.data == 0
        assert self.dll.size == 3

    def test_insert_before_middle(self):
        """Test inserting before an element in the middle"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.insert_before(15, 2)
        assert self.dll.size == 4

    def test_insert_before_nonexistent(self):
        """Test inserting before a nonexistent element"""
        self.dll.insert_at_end(1)
        self.dll.insert_before(0, 999)
        assert self.dll.size == 1

    def test_insert_after_at_tail(self):
        """Test inserting after the tail"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_after(3, 2)
        tail = self.dll.tail
        assert tail is not None
        assert tail.data == 3
        assert self.dll.size == 3

    def test_insert_after_middle(self):
        """Test inserting after an element in the middle"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.insert_after(25, 2)
        assert self.dll.size == 4

    def test_insert_after_nonexistent(self):
        """Test inserting after a nonexistent element"""
        self.dll.insert_at_end(1)
        self.dll.insert_after(0, 999)
        assert self.dll.size == 1

    def test_remove_at_beginning_empty(self):
        """Test removing from beginning of empty list"""
        self.dll.remove_at_beginning()
        assert self.dll.head is None
        assert self.dll.tail is None

    def test_remove_at_beginning_single_element(self):
        """Test removing from beginning when list has one element"""
        self.dll.insert_at_end(1)
        self.dll.remove_at_beginning()
        assert self.dll.head is None
        assert self.dll.tail is None
        assert self.dll.size == 0

    def test_remove_at_beginning_multiple(self):
        """Test removing from beginning with multiple elements"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_at_beginning()
        head = self.dll.head
        assert head is not None
        assert head.data == 2
        assert head.prev is None
        assert self.dll.size == 2

    def test_remove_at_end_empty(self):
        """Test removing from end of empty list"""
        self.dll.remove_at_end()
        assert self.dll.head is None
        assert self.dll.tail is None

    def test_remove_at_end_single_element(self):
        """Test removing from end when list has one element"""
        self.dll.insert_at_end(1)
        self.dll.remove_at_end()
        assert self.dll.head is None
        assert self.dll.tail is None
        assert self.dll.size == 0

    def test_remove_at_end_multiple(self):
        """Test removing from end with multiple elements"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_at_end()
        tail = self.dll.tail
        assert tail is not None
        assert tail.data == 2
        assert tail.next is None
        assert self.dll.size == 2

    def test_remove_by_value_empty(self):
        """Test removing by value in empty list"""
        self.dll.remove(1)
        assert self.dll.size == 0

    def test_remove_by_value_head(self):
        """Test removing head by value"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove(1)
        head = self.dll.head
        assert head is not None
        assert head.data == 2
        assert self.dll.size == 2

    def test_remove_by_value_tail(self):
        """Test removing tail by value"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove(3)
        tail = self.dll.tail
        assert tail is not None
        assert tail.data == 2
        assert self.dll.size == 2

    def test_remove_by_value_middle(self):
        """Test removing middle element by value"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove(2)
        assert self.dll.size == 2

    def test_remove_nonexistent(self):
        """Test removing nonexistent element"""
        self.dll.insert_at_end(1)
        self.dll.remove(999)
        assert self.dll.size == 1

    def test_bidirectional_traversal(self):
        """Test that list maintains proper prev/next references"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        
        # Going forward
        current = self.dll.head
        assert current is not None
        assert current.data == 1
        current = current.next
        assert current is not None
        assert current.data == 2
        current = current.next
        assert current is not None
        assert current.data == 3
        
        # Going backward
        current = self.dll.tail
        assert current is not None
        assert current.data == 3
        current = current.prev
        assert current is not None
        assert current.data == 2
        current = current.prev
        assert current is not None
        assert current.data == 1

    def test_search_exists(self):
        """Test searching for an existing element"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        assert self.dll.search(2) is True
        assert self.dll.search(1) is True
        assert self.dll.search(3) is True

    def test_search_not_exists(self):
        """Test searching for a non-existing element"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        assert self.dll.search(999) is False
        assert self.dll.search(0) is False

    def test_search_empty_list(self):
        """Test searching in an empty list"""
        assert self.dll.search(1) is False

    def test_find_exists(self):
        """Test finding an existing element"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        assert self.dll.find(2) == 2
        assert self.dll.find(1) == 1
        assert self.dll.find(3) == 3

    def test_find_not_exists(self):
        """Test finding a non-existing element"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        assert self.dll.find(999) is None
        assert self.dll.find(0) is None

    def test_find_empty_list(self):
        """Test finding in an empty list"""
        assert self.dll.find(1) is None

    def test_remove_before_middle(self):
        """Test removing the node before a middle element"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_before(3)  # Should remove 2
        assert self.dll.size == 2
        assert list(self.dll) == [1, 3]

    def test_remove_before_second_element(self):
        """Test removing the node before the second element (removes head)"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_before(2)  # Should remove 1
        assert self.dll.size == 2
        head = self.dll.head
        assert head is not None
        assert head.data == 2
        assert head.prev is None

    def test_remove_before_empty(self):
        """Test removing before in empty list"""
        self.dll.remove_before(1)
        assert self.dll.size == 0

    def test_remove_before_single_element(self):
        """Test removing before when only one element exists"""
        self.dll.insert_at_end(1)
        self.dll.remove_before(1)
        assert self.dll.size == 1  # Nothing removed

    def test_remove_after_middle(self):
        """Test removing the node after a middle element"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_after(1)  # Should remove 2
        assert self.dll.size == 2
        assert list(self.dll) == [1, 3]

    def test_remove_after_tail(self):
        """Test removing after tail (nothing to remove)"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_after(3)  # Should not remove anything
        assert self.dll.size == 3

    def test_remove_after_becomes_tail(self):
        """Test that tail pointer is updated when removing after last element"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        self.dll.remove_after(2)  # Should remove 3, making 2 the tail
        tail = self.dll.tail
        assert tail is not None
        assert tail.data == 2
        assert tail.next is None
        assert self.dll.size == 2

    def test_remove_after_empty(self):
        """Test removing after in empty list"""
        self.dll.remove_after(1)
        assert self.dll.size == 0

    def test_iterate_backward_multiple(self):
        """Test iterating backward through list with multiple elements"""
        self.dll.insert_at_end(1)
        self.dll.insert_at_end(2)
        self.dll.insert_at_end(3)
        result = list(self.dll.iterate_backward())
        assert result == [3, 2, 1]

    def test_iterate_backward_single(self):
        """Test iterating backward with single element"""
        self.dll.insert_at_end(1)
        result = list(self.dll.iterate_backward())
        assert result == [1]

    def test_iterate_backward_empty(self):
        """Test iterating backward on empty list"""
        result = list(self.dll.iterate_backward())
        assert result == []

    def test_bidirectional_consistency(self):
        """Test that forward and backward iteration give reversed results"""
        self.dll.insert_at_end(10)
        self.dll.insert_at_end(20)
        self.dll.insert_at_end(30)
        self.dll.insert_at_end(40)
        forward = list(self.dll)
        backward = list(self.dll.iterate_backward())
        assert forward == list(reversed(backward))
