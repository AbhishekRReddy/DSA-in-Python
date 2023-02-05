class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class Circular_Linked_List:
    def __init__(self,node=None):
        self.head=node
        self.tail=node
        self.length=0
    
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
        self.length=1
        return 'CircularSLL is created'

    def insertion(self,value,location):
        if(location>=self.length):
            print('Invalid Location given')
            return

        if self.head is None:
            print('The Linked List does not exist')
        
        else:
            new_node=Node(value)
            if location==0:
                new_node.next=self.head
                self.tail.next=new_node
                self.head=new_node
                self.length+=1
                return
            elif location==-1:
                new_node.next=self.head
                self.tail.next=new_node
                self.tail=new_node
                self.length+=1
                return
            else:
                index=0
                pointer=self.head
                while pointer:
                    if(index==location-1):
                        new_node.next=pointer.next
                        pointer.next=new_node
                        self.length+=1
                        return
                    index+=1
                    pointer=pointer.next
                    if(pointer==self.head):
                        print('Invalid location is given')
                        break
    def traverse(self):
        if self.head is None:
            print('Linked List does not exists')
        else:
            pointer=self.head
            while pointer:
                print(pointer.value)
                if(pointer.next==self.head):
                    break
                pointer=pointer.next
    def search(self,search_value):
        pointer=self.head
        counter=0
        while pointer:
            if(pointer.value==search_value):
                print(f'{search_value} found at location {counter}')
                return
            if(pointer==self.tail):
                print('Value not found and you have reached end of the CSLL')
                return
            pointer=pointer.next
            counter+=1

    def deletion(self,location):
        if self.head is None:
            print('Linked List does not Exist')
            return
        if location>=self.length:
            print('Invalid location number is given')
            return 
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                    self.length-=1
                    return
                else:
                    self.head=self.head.next
                    self.tail.next=self.tail.next.next
                    self.length-=1
                    return
            elif location==-1:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None
                    self.length-=1
                    return
                else:
                    pointer=self.head
                    while pointer:
                        if(pointer.next.next == self.head):
                            break
                        pointer=pointer.next
                    pointer.next=self.head
                    self.tail=pointer
                    self.length-=1
                    return
            else:
                counter=0
                pointer=self.head
                while pointer:
                    if(counter==location-1):
                        pointer.next=pointer.next.next
                        self.length-=1
                        return
                    pointer=pointer.next
                    counter+=1
                    if(pointer==self.head):
                        print('Invalid location is given')
                        break
                    
                

 
csll=Circular_Linked_List()
csll.createSCLL(1)

csll.insertion(101,0)
csll.insertion(14,1)
csll.insertion(45,0)
print([node.value for node in csll])
csll.deletion(4)
print([node.value for node in csll])
