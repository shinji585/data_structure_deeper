"""
Test suite for SinglyLinkedList implementation
"""

from linkendlist.singlylinkedlist import SinglyLinkedList


class TestSinglyLinkedList:
    """Tests for SinglyLinkedList implementation"""

    def setup_method(self):
        """Setup method to initialize a fresh list before each test"""
        self.sll: SinglyLinkedList[int] = SinglyLinkedList()

    def test_insert_at_beginning_empty_list(self):
        """Test inserting at beginning in an empty list"""
        self.sll.insert_at_beginning(10)
        head = self.sll.head
        tail = self.sll.tail
        assert head is not None
        assert head.data == 10
        assert tail is not None
        assert tail.data == 10
        assert self.sll.size == 1

    def test_insert_at_beginning_multiple(self):
        """Test inserting multiple elements at beginning"""
        self.sll.insert_at_beginning(1)
        self.sll.insert_at_beginning(2)
        self.sll.insert_at_beginning(3)
        head = self.sll.head
        tail = self.sll.tail
        assert head is not None
        assert head.data == 3
        assert tail is not None
        assert tail.data == 1
        assert self.sll.size == 3

    def test_insert_at_end_empty_list(self):
        """Test inserting at end in an empty list"""
        self.sll.insert_at_end(10)
        head = self.sll.head
        tail = self.sll.tail
        assert head is not None
        assert head.data == 10
        assert tail is not None
        assert tail.data == 10
        assert self.sll.size == 1

    def test_insert_at_end_multiple(self):
        """Test inserting multiple elements at end"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        head = self.sll.head
        tail = self.sll.tail
        assert head is not None
        assert head.data == 1
        assert tail is not None
        assert tail.data == 3
        assert self.sll.size == 3

    def test_insert_before_at_head(self):
        """Test inserting before the head"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_before(0, 1)
        head = self.sll.head
        assert head is not None
        assert head.data == 0
        assert self.sll.size == 3

    def test_insert_before_middle(self):
        """Test inserting before an element in the middle"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.insert_before(15, 2)
        assert self.sll.size == 4

    def test_insert_before_nonexistent(self):
        """Test inserting before a nonexistent element"""
        self.sll.insert_at_end(1)
        self.sll.insert_before(0, 999)
        assert self.sll.size == 1  # Size doesn't change

    def test_insert_after_at_tail(self):
        """Test inserting after the tail"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_after(3, 2)
        tail = self.sll.tail
        assert tail is not None
        assert tail.data == 3
        assert self.sll.size == 3

    def test_insert_after_middle(self):
        """Test inserting after an element in the middle"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.insert_after(25, 2)
        assert self.sll.size == 4

    def test_insert_after_nonexistent(self):
        """Test inserting after a nonexistent element"""
        self.sll.insert_at_end(1)
        self.sll.insert_after(0, 999)
        assert self.sll.size == 1  # Size doesn't change

    def test_remove_at_beginning_empty(self):
        """Test removing from beginning of empty list"""
        self.sll.remove_at_beginning()
        assert self.sll.head is None
        assert self.sll.tail is None

    def test_remove_at_beginning_single_element(self):
        """Test removing from beginning when list has one element"""
        self.sll.insert_at_end(1)
        self.sll.remove_at_beginning()
        assert self.sll.head is None
        assert self.sll.tail is None
        assert self.sll.size == 0

    def test_remove_at_beginning_multiple(self):
        """Test removing from beginning with multiple elements"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove_at_beginning()
        head = self.sll.head
        assert head is not None
        assert head.data == 2
        assert self.sll.size == 2

    def test_remove_at_end_empty(self):
        """Test removing from end of empty list"""
        self.sll.remove_at_end()
        assert self.sll.head is None
        assert self.sll.tail is None

    def test_remove_at_end_single_element(self):
        """Test removing from end when list has one element"""
        self.sll.insert_at_end(1)
        self.sll.remove_at_end()
        assert self.sll.head is None
        assert self.sll.tail is None
        assert self.sll.size == 0

    def test_remove_at_end_multiple(self):
        """Test removing from end with multiple elements"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove_at_end()
        tail = self.sll.tail
        assert tail is not None
        assert tail.data == 2
        assert self.sll.size == 2

    def test_remove_by_value_empty(self):
        """Test removing by value in empty list"""
        self.sll.remove(1)
        assert self.sll.size == 0

    def test_remove_by_value_head(self):
        """Test removing head by value"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove(1)
        head = self.sll.head
        assert head is not None
        assert head.data == 2
        assert self.sll.size == 2

    def test_remove_by_value_tail(self):
        """Test removing tail by value"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove(3)
        tail = self.sll.tail
        assert tail is not None
        assert tail.data == 2
        assert self.sll.size == 2

    def test_remove_by_value_middle(self):
        """Test removing middle element by value"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove(2)
        assert self.sll.size == 2

    def test_remove_nonexistent(self):
        """Test removing nonexistent element"""
        self.sll.insert_at_end(1)
        self.sll.remove(999)
        assert self.sll.size == 1
