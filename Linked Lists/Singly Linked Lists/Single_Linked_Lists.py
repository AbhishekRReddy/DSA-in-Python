class LinkedLists:
    def __init__(self,node=None):
        self.head=node
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def insertion(self,value,location):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        else:
            if location==0:
                new_node.next=self.head
                self.head=new_node
                return
            elif location==-1:
                new_node.next=None
                self.tail.next=new_node
                self.tail=new_node
            else:
                counter=0
                pointer=self.head
                while pointer.next:
                    if(counter==location):
                        new_node.next=pointer.next
                        pointer.next=new_node
                        return 
                    counter+=1
                    pointer=pointer.next

    def traverse(self):
        if self.head is None:
            print('No elements are found in Linked Lists')

        else:
            node=self.head
            while node:
                print(node.value)
                node=node.next

    def search(self,nodeValue):
        if self.head is None:
            return 'Linked List does not Exist'
        else:
            node=self.head
            index=0
            while node:
                if(node.value==nodeValue):
                    return f'{node.value} found at index position of {index}'
                node=node.next
                index+=1
            return f'{node.value} is not present in the Linked List'


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

    

ll=LinkedLists()
ll.insertion(5,0)
ll.insertion(6,0)

ll.insertion(99,-1)
print([node.value for node in ll])
print(ll.search(99))