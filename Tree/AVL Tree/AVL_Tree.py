from Queue_Using_Linked_Lists import Queue
class Node:
    def __init__(self, value = None):
        self.data = value
        self.left_child = None
        self.right_child = None
        self.height = 1

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

def level_order_traverse(node):
    if node is None:
        print("Tree is empty")
        return
    queue = Queue()
    queue.enqueue(node)
    while not queue.isEmpty():
        temp_node = queue.dequeue()
        print(temp_node.value.data)
        if temp_node.value.left_child:
            queue.enqueue(temp_node.value.left_child)
        if temp_node.value.right_child:
            queue.enqueue(temp_node.value.right_child)

def search(node , value):
    if node is None:
        print('Element does not exists anywhere')
        return
    elif node.data == value:
        print('Element does exists in the tree')
        return
    elif node.data > value:
        search(node.left_child, value)
    elif node.data < value:
        search(node.right_child, value)

def get_height(node):
    if node is None:
        return 0
    return node.height


    









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

search(root_node, 600)