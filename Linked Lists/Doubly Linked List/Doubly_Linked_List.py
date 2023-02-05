class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def create_DLL(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
    print('The Doubly Linked List created')

    
dll=DLL()
dll.create_DLL(0)
print([node.value for node in dll])

