class BSTNode:
    def __init__(self, value=None):
        self.data = value
        self.left_node = None
        self.right_node = None

class BST:
    def __init__(self,value = None):
        self.root = None

    def core_insert_node(self, node, value):
        if value <= node.data:
            if node.left_node == None:
                node.left_node = BSTNode(value)
            else:
                self.core_insert_node(node.left_node , value)
        else:
            if node.right_node == None:
                node.right_node = BSTNode(value)
            else:
                self.core_insert_node(node.right_node, value)
        print('Node has been successfully inserted')
    def insert_node(self, value):
        if self.root is None:
            self.root = BSTNode(value)
            return
        else:
            self.core_insert_node(self.root, value)


    def core_inorder_traverse(self, node):
        if node is None:
            return
        self.core_inorder_traverse(node.left_node)
        print(node.data)
        self.core_inorder_traverse(node.right_node)
    
    def inorder_traverse(self):
        self.core_inorder_traverse(self.root)


bst = BST()

for i in range(50,0,-1):
    bst.insert_node(i)
    
bst.inorder_traverse()

