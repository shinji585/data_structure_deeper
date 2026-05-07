from tree.tree_node import  Node



class TestTreeNode:

    def setup_method(self):
        self.n1: Node[int] = Node(data=None)  # type: ignore[call-arg]

    def test_create_nodes_adds(self):
        n2: Node[int] = Node(data=20)
        n3: Node[int] = Node(data=30)
        n4: Node[int] = Node(data=50)

        if self.n1 is None:
            self.n1 = n3
            self.n1.left_child = n2
            self.n1.right_child = n4
        else:
            self.n1.right_child = n3 # type: ignore[assignment]
            self.n1.left_child = n2 # type: ignore[assignment]
            n2.left_child = n4 # type: ignore[assignment]

