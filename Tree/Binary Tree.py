import Queue_Using_Linked_Lists as queue

class TreeNode:
    def __init__(self, data):
        self.value = data
        self.leftNode = None
        self.rightNode = None
    
bt  = TreeNode(1)
nodeA = TreeNode(2)
nodeB = TreeNode(3)
nodeC = TreeNode(4)
nodeD = TreeNode(5)
nodeE = TreeNode(6)
NodeF = TreeNode(7)
bt.leftNode = nodeA
bt.rightNode = nodeB
nodeA.leftNode = nodeC
nodeA.rightNode = nodeD
nodeB.leftNode = nodeE
nodeB.rightNode = NodeF

def preOrderTraverse(rootNode):
    if not rootNode:
        return
    print(rootNode.value)
    preOrderTraverse(rootNode.leftNode)
    preOrderTraverse(rootNode.rightNode)

def inOrderTraverse(rootNode):
    if not rootNode:
        return
    inOrderTraverse(rootNode.leftNode)
    print(rootNode.value)
    inOrderTraverse(rootNode.rightNode)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftNode)
    postOrderTraversal(rootNode.rightNode)
    print(rootNode.value)

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            element = customQueue.dequeue()
            return element.value.value
            if element.value.leftNode is not None:
                customQueue.enqueue(element.value.leftNode)
            if element.value.rightNode is not None:
                customQueue.enqueue(element.value.rightNode)

def search(rootNode, value):
    if not rootNode:
        return 'Binary Tree is Empty'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            node = customQueue.dequeue()
            if node.value.value == value:
                return 'Value is found in Binary Tree'
            if node.value.leftNode is not None:
                customQueue.enqueue(node.value.leftNode)
            if node.value.rightNode is not None:
                customQueue.enqueue(node.value.rightNode)
        return 'Value is not found in the BT'

for i in range(1, 8):
    print(search(bt,i))
print(search(bt,10))
