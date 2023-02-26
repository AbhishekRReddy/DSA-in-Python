from Queue_Using_Linked_Lists import Queue
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
            print(node.data,end = '--')
            self.core_pre_order_traversal(node.left_node)
            self.core_pre_order_traversal(node.right_node)
    
    def pre_order_traversal(self):
        self.core_pre_order_traversal(self.root)

    def core_post_order_traversal(self, node):
        if node:
            self.core_post_order_traversal(node.left_node)
            self.core_post_order_traversal(node.right_node)
            print(node.data, end = '--')

    def post_order_traversal(self):
        self.core_post_order_traversal(self.root)

    def core_search(self, node, value):
        if node is None:
            return 'Value does not exists'
        elif node.data == value:
            return 'Value is found'
        else:
            if node.data >= value:
                return self.core_search(node.left_node, value)
            else:
                return self.core_search(node.right_node, value)

    def level_order_traversal(self):
        if self.root is None:
            return 'The BST is empty'
        queue =[]
        queue.append(self.root)
        while len(queue)>0:
            node = queue.pop(0)
            print(node.data,end='--')
            if node.left_node:
                queue.append(node.left_node)
            if node.right_node: 
                queue.append(node.right_node)






    def search(self, value):
        return self.core_search(self.root, value)




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
print('--------------------------------')
bst.level_order_traversal()
