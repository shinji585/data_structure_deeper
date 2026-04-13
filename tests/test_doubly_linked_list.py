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
