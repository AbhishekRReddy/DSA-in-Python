'''
Linked Lists implementation using the python

'''
#Function to initiate the Node class
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    #Inserting the element at the beginning
    def insert_at_start(self,data):
        node=Node(data,self.head)
        self.head=node

    #Append the List from the beginning of the Linked Lists 
    #Pass the order as True in case the elements have to be ordered in the same order.
    def insert_from_list(self,elements,order=True):
        if order:
            for element in reversed(elements):
                self.insert_at_start(element)
        else:
            for element in elements:
                self.insert_at_start(element)

    def insert_at_end(self,data):
        #Check if the Linked List is empty
        if self.head is None:
            self.insert_at_start(data)
            return
        pointer=self.head
        while pointer.next:
            pointer=pointer.next
        pointer.next=Node(data)

    #Function to insert the element after sepcific node value
    #The data in the existing node is given
    def insert_after_node(self,existing_value,data):
        pointer=self.head
        while pointer:
            if(pointer.data==existing_value):
                node=Node(data,pointer.next)
                pointer.next=node
                return
            pointer=pointer.next


    def printlist(self):
        pointer=self.head
        while(pointer):
            print(str(pointer.data)+"-->",end="")
            pointer=pointer.next
        print('')
ll=LinkedList()
ll.insert_from_list([1,2,3,4,5,6,7,8])
ll.printlist()
ll.insert_after_node(4,99)
ll.printlist()
