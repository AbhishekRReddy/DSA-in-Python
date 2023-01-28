'''
Implementation of Linekd list using the python.

1.We will class for the Element.
2.We will have seprate class for the Linked List
'''
class Element:
    def __init__(self, value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    
    def append(self,new_element):
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=new_element

