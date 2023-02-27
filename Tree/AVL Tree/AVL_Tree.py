class Node:
    def __init__(self, value = None):
        self.data = value
        self.left_child = None
        self.right_child = None

def pre_order_traverse(node):
    if node is None:
        return
    print(node.data)
    pre_order_traverse(node.left_child)
    pre_order_traverse(node.right_child)

def post_order_traverse(node):
    if node is None:
        return
    post_order_traverse(node.left_child)
    post_order_traverse(node.right_child)
    print(node.data, end = '--')

def inorder_traverse(node):
    if node is None:
        return
    inorder_traverse(node.left_child)
    print(node.data, end = '--')
    inorder_traverse(node.right_child)








root_node = Node(70)
node50 = Node(50)
node60 = Node(60)
node90 = Node(90)
node30 = Node(30)
node20 = Node(20)
node40 = Node(40)
node90 = Node(90)
node80 = Node(80)
node100 = Node(100)
root_node.left_child = node50
root_node.right_child = node90
node50.left_child = node30
node50.right_child = node60 
node30.left_child = node20
node30.right_child = node40
node90.left_child = node80
node90.right_child = node100

inorder_traverse(root_node)