import Queue_Using_Linked_Lists as queue

class TreeNode:
    def __init__(self, data):
        self.value = data
        self.leftNode = None
        self.rightNode = None
    
    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self, node = None):
        self.root = node

    def core_preOrderTraverse(self, rootNode):
        if rootNode is None:
            return
        print(rootNode.value)
        self.core_preOrderTraverse(rootNode.leftNode)
        self.core_preOrderTraverse(rootNode.rightNode)
    
    def PreOrderTraverse(self):
        self.core_preOrderTraverse(self.root)

    def core_inOrderTraverse(self, rootNode):
        if rootNode is None:
            return
        self.core_inOrderTraverse(rootNode.leftNode)
        print(rootNode.value)
        self.core_inOrderTraverse(rootNode.rightNode)

    def inOrderTraverse(self):
        self.core_inOrderTraverse(self.root)




    
bt  = TreeNode(1)
tree = BinaryTree(bt)

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
            print(element.value.value)
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

def preOrderSearch(rootNode, value):
    if not rootNode:
        return False
    if rootNode.value == value:
        return True
    if preOrderSearch(rootNode.leftNode, value):
        return True
    if preOrderSearch(rootNode.rightNode, value):
        return True
    return False

def levelOrderInsertion(rootNode, element_value):
    newNode = TreeNode(element_value)
    if rootNode is None:
        rootNode = newNode
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            node = customQueue.dequeue()
            if node.value.leftNode is not None:
                customQueue.enqueue(node.value.leftNode)
            else:
                node.value.leftNode = newNode
                return 'Node has been successfully inserted'
            if node.value.rightNode is not None:
                customQueue.enqueue(node.value.rightNode)
            else:
                node.value.rightNode = newNode
                return 'Node has been successfully inserted'


def getDeeepestNode(rootNode):
    if rootNode is None:
        return 'Binary Tree is Empty'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            tempNode = customQueue.dequeue()
            if tempNode.value.leftNode is not None:
                customQueue.enqueue(tempNode.value.leftNode)
            if tempNode.value.rightNode is not None:
                customQueue.enqueue(tempNode.value.rightNode)
        deepestNode = tempNode.value
        return deepestNode

def deleteDeepestNode(rootNode, deepestNode):
    if rootNode is None:
        return 'Binary Tree is Empty'
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            current_node = customQueue.dequeue()
            if current_node.value is deepestNode:
                current_node.value = None
                return

            if current_node.value.leftNode:
                if current_node.value.leftNode is deepestNode:
                    current_node.value.leftNode = None
                    return
                else:
                    customQueue.enqueue(current_node.value.leftNode)

            if current_node.value.rightNode:
                if current_node.value.rightNode is deepestNode:
                    current_node.value.rightNode = None
                    return
                else:
                    customQueue.enqueue(current_node.value.rightNode)


tree.inOrderTraverse()


