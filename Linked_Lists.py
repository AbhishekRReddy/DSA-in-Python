'''
Implementation of Linekd list using the python.

1.We will class for the Element.
2.We will have seprate class for the Linked List
'''
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    
    def insert_at_beginning(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print('Linked List is Empty')
            return
        else:
            itr=self.head
            llstr=''
            while itr:
                llstr+=str(itr.data)+'-->'
                itr=itr.next
            print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return None
        else:
            itr=self.head
            while itr.next:
                itr=itr.next    
            itr.next=Node(data,None) 
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        itr=self.head
        counter=0
        while itr:
            counter+=1
            itr=itr.next
        return counter
    def remove(self,position):
        if position<0 or position>=self.get_length():
            raise Exception("Invalid Index")
        pointer=self.head
        if(position==0):
            self.head=pointer.next
            return
        counter=0
        while pointer:
            if(counter==position-1):
                pointer.next=pointer.next.next
                break
            counter+=1
            pointer=pointer.next
     
    def insert_at(self,position,data):
        if position<0 or position>=self.get_length():
            raise Exception("Invalid Index")
        if position==0:
            temp=self.head
            self.head=Node(data,temp)
        else:
            pointer=self.head
            counter=0
            while pointer:
                if(counter==position-1):
                    temp=pointer.next
                    pointer.next=Node(data,temp)
                    break
                counter+=1
                pointer=pointer.next

'''
-----------------------------------------------------------------------------------------------------------------
''' 

ll=LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(6)
ll.insert_at_beginning(7)
ll.insert_at_end(10)
ll.insert_values([1,3,4,5,6,8,9,6,7])

ll.print()
ll.insert_at(2,777)
ll.print()


