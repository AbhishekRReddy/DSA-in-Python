class LinkedLists:
    def __init__(self,node=None):
        self.head=node
        self.tail=None

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    

ll=LinkedLists()
node1=Node(1)
node2=Node(2)
ll.head=node1
ll.head.next=node2
ll.tail=node2