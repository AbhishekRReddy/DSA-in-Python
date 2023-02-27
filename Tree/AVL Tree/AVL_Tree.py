class Node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None

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
