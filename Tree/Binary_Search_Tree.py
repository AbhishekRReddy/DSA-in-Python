class BSTNode:
    def __init__(self, value):
        self.data = value
        self.left_node = None
        self.right_node = None

class BST:
    def __init__(self,value = None):
        self.root = BSTNode(value)

