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



inOrderTraverse(bt)