from Stack_and_Queue.Queues import ListQueue

class TestQueues:
    """Tests for ListQueue implementation"""

    def setup_method(self):
        self.dl1: ListQueue[int] = ListQueue()

    def test_enqueue(self):
        """Test enqueue operation"""
        self.dl1.enqueue(data=10)
        self.dl1.enqueue(data=20)
        self.dl1.enqueue(data=30)
        self.dl1.enqueue(data=40)
        self.dl1.enqueue(data=50)


        assert  len(self.dl1.items) == 5
        assert  self.dl1.items[0] == 50

    def test_dequeue(self):
        """Test dequeue operation"""
        self.dl1.dequeue()
        self.dl1.dequeue()

        removed = self.dl1.dequeue()

        assert  removed == 10
        assert len(self.dl1.items) == 4

    def test_dequeue_empty(self):
        """Test queue empty"""
        result = self.dl1.dequeue()
        assert result is None