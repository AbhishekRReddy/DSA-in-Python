import Queue_Using_Linked_Lists as queue

class TreeNode:
    def __init__(self, data):
        self.value = data
        self.leftNode = None
        self.rightNode = None
    
    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self, value = None):
        self.root = TreeNode(value)

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

    def core_postOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.core_postOrderTraversal(rootNode.leftNode)
        self.core_postOrderTraversal(rootNode.rightNode)
        print(rootNode.value)
    def postOrderTraversal(self):
        self.core_postOrderTraversal(self.root)
    
    def levelOrder(self):
        if not self.root:
            return
        else:
            customQueue = queue.Queue()
            customQueue.enqueue(self.root)
            while not customQueue.isEmpty():
                element = customQueue.dequeue()
                print(element.value.value)
                if element.value.leftNode is not None:
                    customQueue.enqueue(element.value.leftNode)
                if element.value.rightNode is not None:
                    customQueue.enqueue(element.value.rightNode)

    def search(self, value):
        if not self.root:
            return 'Binary Tree is Empty'
        else:
            customQueue = queue.Queue()
            customQueue.enqueue(self.root)
            while not customQueue.isEmpty():
                node = customQueue.dequeue()
                if node.value.value == value:
                    return 'Value is found in Binary Tree'
                if node.value.leftNode is not None:
                    customQueue.enqueue(node.value.leftNode)
                if node.value.rightNode is not None:
                    customQueue.enqueue(node.value.rightNode)
            return 'Value is not found in the BT'

    def core_preOrderSearch(self, rootNode, value):
        if not rootNode:
            return False
        if rootNode.value == value:
            return True
        if self.core_preOrderSearch(rootNode.leftNode, value):
            return True
        if self.core_preOrderSearch(rootNode.rightNode, value):
            return True
        return False

    def preOrderSearch(self, value):
        return self.core_preOrderSearch(self.root, value)

    def levelOrderInsertion(self, element_value):
        newNode = TreeNode(element_value)
        if self.root is None:
            self.root = newNode
        else:
            customQueue = queue.Queue()
            customQueue.enqueue(self.root)
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

    def getDeeepestNode(self):
        if self.root is None:
            return 'Binary Tree is Empty'
        else:
            customQueue = queue.Queue()
            customQueue.enqueue(self.root)
            while not(customQueue.isEmpty()):
                tempNode = customQueue.dequeue()
                if tempNode.value.leftNode is not None:
                    customQueue.enqueue(tempNode.value.leftNode)
                if tempNode.value.rightNode is not None:
                    customQueue.enqueue(tempNode.value.rightNode)
            deepestNode = tempNode.value
            return deepestNode

    def deleteDeepestNode(self):
        deepestNode = self.getDeeepestNode()
        if self.root is None:
            return 'Binary Tree is Empty'
        else:
            if self.root is deepestNode:
                self.root = None
            else:
                customQueue = queue.Queue()
                customQueue.enqueue(self.root)
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


btree = BinaryTree(1)
'''
for i in range(2, 8):
    btree.levelOrderInsertion(i)
    '''
btree.levelOrder()
print('---------------------------------------------')
btree.deleteDeepestNode()
btree.levelOrder()
