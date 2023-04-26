class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self,node):
        self.head=node
    
    def push(self,node):
        pointer=self.head
        node.next=self.head
        self.head=node

    def get_length_iter(self):
        pointer=self.head
        counter=0
        while pointer:
            counter+=1
            pointer=pointer.next
        return counter

    def get_length_recur(self,node):
        if(node is None):
            return 0 
        else:
            return 1+self.get_length_recur(node.next)

    def get_length_recur_tail(self,node,counter=0):
        if(node is None):
            return counter
        else:
            return self.get_length_recur_tail(node.next,counter+1)

    def get_length_driver(self):
        return self.get_length_recur_tail(self.head)

'''
-----------------------------------------------------------------------------------------------
'''
if __name__=='__main__':
    e1=Node(1)
    e2=Node(2)
    e3=Node(3)
    e4=Node(4)
    ll=LinkedList(e1)
    ll.push(e2)
    ll.push(e3)
    ll.push(e4)
    print(ll.get_length_driver())

