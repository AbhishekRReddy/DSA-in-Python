class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def create_DLL(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1
        print('The Doubly Linked List created')

    def insertion(self,value,location):
        if(location>=self.length):
            print("Invalid Location is Given")
            return
        if(self.head is None):
            print('Linked List does not Exist')
            return
        else:
            new_node=Node(value)
            if location==0:
                new_node.next=self.head
                new_node.prev=None
                self.head.prev=new_node
                self.head=new_node
                self.length+=1
                return
            elif location==-1:
                new_node.prev=self.tail
                self.tail.next=new_node
                self.tail=new_node
                self.length+=1
                return
            else:
                counter=0
                pointer=self.head
                while counter<location-1:
                    pointer=pointer.next
                    counter+=1
                new_node.prev=pointer 
                new_node.next=pointer.next
                pointer.next.prev=new_node
                pointer.next=new_node
                self.length+=1
                return 

    def traverse(self):
        if self.head is None:
            print('Linked List does not exists')
            return
        else:
            pointer = self.head
            while pointer:
                print(pointer.value)
                pointer = pointer.next
           
    def reverse_traverse(self):
        if self.head is None:
            print('Linked Lists does not exists')
        else:
            pointer=self.tail
            while pointer:
                print(pointer.value)
                pointer = pointer.prev
        
    def find_value(self,value):
        if self.head is None:
            print('Linked list does not exist')
            return
        else:
            counter=0
            pointer = self.head
            while pointer:
                if(pointer.value==value):
                    print(f'{value} found at location {counter}')
                    return
                pointer = pointer.next
                counter += 1
            print(f'{value} does not exist in the Linked List')


dll=DLL()
dll.create_DLL(0)
dll.insertion(1,-1)
dll.insertion(2,-1)
dll.insertion(3,-1)
dll.insertion(4,-1)
dll.insertion(-1,0)
print([node.value for node in dll])
print(dll.length)
dll.insertion(7,5)

print([node.value for node in dll])
dll.find_value(78)


