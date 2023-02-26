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
        print(node.data,end='--')
        self.core_inorder_traverse(node.right_node)
    
    def inorder_traverse(self):
        self.core_inorder_traverse(self.root)

    def core_pre_order_traversal(self, node):
        if node:
            print(node.data,end='--')
            self.core_pre_order_traversal(node.left_node)
            self.core_pre_order_traversal(node.right_node)

    def pre_order_traversal(self):
        self.core_pre_order_traversal(self.root)


bst = BST()

bst.insert_node(5)
bst.insert_node(4)
bst.insert_node(9)
bst.insert_node(6)
bst.insert_node(10)
bst.insert_node(2)
bst.insert_node(3)
bst.insert_node(1)
bst.insert_node(7)
    
bst.pre_order_traversal()

