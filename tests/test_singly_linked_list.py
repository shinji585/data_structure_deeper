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

    def test_search_exists(self):
        """Test searching for an existing element"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        assert self.sll.search(2) is True
        assert self.sll.search(1) is True
        assert self.sll.search(3) is True

    def test_search_not_exists(self):
        """Test searching for a non-existing element"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        assert self.sll.search(999) is False
        assert self.sll.search(0) is False

    def test_search_empty_list(self):
        """Test searching in an empty list"""
        assert self.sll.search(1) is False

    def test_find_exists(self):
        """Test finding an existing element"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        assert self.sll.find(2) == 2
        assert self.sll.find(1) == 1
        assert self.sll.find(3) == 3

    def test_find_not_exists(self):
        """Test finding a non-existing element"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        assert self.sll.find(999) is None
        assert self.sll.find(0) is None

    def test_find_empty_list(self):
        """Test finding in an empty list"""
        assert self.sll.find(1) is None

    def test_remove_before_middle(self):
        """Test removing the node before a middle element"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove_before(3)  # Should remove 2
        assert self.sll.size == 2
        assert list(self.sll) == [1, 3]

    def test_remove_before_second_element(self):
        """Test removing the node before the second element (removes head)"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove_before(2)  # Should remove 1
        assert self.sll.size == 2
        head = self.sll.head
        assert head is not None
        assert head.data == 2

    def test_remove_before_empty(self):
        """Test removing before in empty list"""
        self.sll.remove_before(1)
        assert self.sll.size == 0

    def test_remove_before_single_element(self):
        """Test removing before when only one element exists"""
        self.sll.insert_at_end(1)
        self.sll.remove_before(1)
        assert self.sll.size == 1  # Nothing removed

    def test_remove_after_middle(self):
        """Test removing the node after a middle element"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove_after(1)  # Should remove 2
        assert self.sll.size == 2
        assert list(self.sll) == [1, 3]

    def test_remove_after_tail(self):
        """Test removing after tail (nothing to remove)"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove_after(3)  # Should not remove anything
        assert self.sll.size == 3

    def test_remove_after_becomes_tail(self):
        """Test that tail pointer is updated when removing after last element"""
        self.sll.insert_at_end(1)
        self.sll.insert_at_end(2)
        self.sll.insert_at_end(3)
        self.sll.remove_after(2)  # Should remove 3, making 2 the tail
        tail = self.sll.tail
        assert tail is not None
        assert tail.data == 2
        assert self.sll.size == 2

    def test_remove_after_empty(self):
        """Test removing after in empty list"""
        self.sll.remove_after(1)
        assert self.sll.size == 0
