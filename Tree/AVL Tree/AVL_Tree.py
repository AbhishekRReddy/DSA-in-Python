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
        print(temp_node.value.data, end = ' ')
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

def right_rotation(disbalanced_node):
    new_root = disbalanced_node.left_child
    disbalanced_node.left_child = disbalanced_node.left_child.right_child
    new_root.right_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height = 1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root

def left_rotation(disbalanced_node):
    new_root = disbalanced_node.right_child
    disbalanced_node.right_child = disbalanced_node.right_child.left_child
    new_root.left_child = disbalanced_node
    disbalanced_node.height = 1 + max(get_height(disbalanced_node.left_child), get_height(disbalanced_node.right_child))
    new_root.height =1 + max(get_height(new_root.left_child), get_height(new_root.right_child))
    return new_root 

def get_balance(node):
    if node is None:
        return 0
    return get_height(node.left_child) - get_height(node.right_child)

def insert(root_node, value):
    if root_node is None:
        return Node(value)
    else:
        if value < root_node.data:
            root_node.left_child = insert(root_node.left_child, value)
        else:
            root_node.right_child = insert(root_node.right_child, value)
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))

    balance = get_balance(root_node)
    #Checking for LL condition
    if balance > 1 and value < root_node.left_child.data:
        return right_rotation(root_node)
    #Checkimg for the LR condition
    if balance > 1 and value > root_node.left_child.data:
        root_node.left_child = left_rotation(root_node.left_child)
        return right_rotation(root_node)
    #Checking for RR Condition
    if balance < -1 and value > root_node.right_child.data:
        return left_rotation(root_node)
    #Checking for the RL rotation:
    if balance < -1 and value < root_node.right_child.data:
        root_node.right_child = right_rotation(root_node.right_child)
        return left_rotation(root_node)
    return root_node

def minimum_value(node):
    if node is None or node.left_child is None:
        return node
    return minimum_value(node.left_child)

def delete_node(node, value):
    if node is None:
        return None
    elif value < node.data:
        node.left_child = delete_node(node.left_child, value)
    elif value > node.data:
        node.right_child = delete_node(node.right_child, value)
    else:
        # We reached the node that we wanted to delete
        #The below two conditions applicable for the nodes with no children
        #or one children
        if node.left_child is None:
            temp = node.right_child
            node = None
            return temp
        if node.right_child is None:
            temp = node.left_child
            node = None
            return temp
        
        temp_node = minimum_value(node.right_child)
        node.data = temp_node.data
        node.right_child = delete_node(node.right_child, temp_node.data)
    node.height = 1 + max(get_height(node.left_child), get_height(node.right_child))
    balance = get_balance(node)
    if balance > 1 and (node.left_child and node.left_child.left_child): 
        return right_rotation(node)
    if balance > 1 and (node.left_child and node.left_child.right_child):
        node.left_child = left_rotation(node.left_child)
        return right_rotation(node)    
    if balance < -1 and (node.right_child and get_balance(node.right_child) <=0):
        return left_rotation(node)
    if balance < -1 and (node.right_child and node.right_child.left_child):
        node.right_child = right_rotation(node.right_child)
        return left_rotation(node)    
    return node


def delete_tree(root_node):
    root_node = None
    return root_node





    
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



my_tree = Node(10)
for i in range(20,100,10):
    my_tree = insert(my_tree, i)

level_order_traverse(my_tree)
my_tree = delete_node(my_tree, 50)
print('--------------------------------------')
my_tree = delete_tree(my_tree)
