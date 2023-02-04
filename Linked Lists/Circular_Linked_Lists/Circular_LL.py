class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class Circular_Linked_List:
    def __init__(self,node=None):
        self.head=node
        self.tail=node
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            if(node.next==self.head):
                break
            node=node.next

    def createSCLL(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        return 'CircularSLL is created'

csll=Circular_Linked_List()
csll.createSCLL(1)
print([node.value for node in csll])