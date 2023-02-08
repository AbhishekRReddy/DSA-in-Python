class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class Cdll:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer
            pointer = pointer.next
            if pointer == self.head:
                break

    def create_cdll(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node
        self.length += 1

    def insertion(self,value,location):
        if location >= self.length:
            print('Invalid location is given')
            return
        if self.head is None:
            print('Linked List is Empty')
            return
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
                self.length += 1
                return
            elif location in [-1,self.length-1]:
                newNode.next = self.head
                newNode.prev = self.tail
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
                self.length += 1
            else:
                index = 0
                pointer = self.head
                while index < location-1:
                    pointer = pointer.next
                    index +=1
                newNode.next = pointer.next
                newNode.prev = pointer
                pointer.next.prev = newNode
                pointer.next = newNode
                self.length += 1
        
    def traverse(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            pointer = self.head
            while pointer:
                print(pointer.value,end='-->')
                pointer=pointer.next
                if(pointer == self.head):
                    print('To start')
                    return

    def reverse_traverse(self):
        if self.tail is None:
            print('Linked list is empty')
        else:
            pointer = self.tail
            while pointer:
                print(pointer.value,end='-->')
                pointer = pointer.prev
                if(pointer == self.tail):
                    print('To End')
                    return

    def search(self,value):
        if self.head is None:
            print('The Linked List is Empty')
        else:
            pointer = self.head
            counter = 0
            while pointer:
                if(pointer.value == value):
                    print(f'{value} found at position of {counter}')
                    return
                pointer = pointer.next
                counter +=1
                if pointer == self.head:
                    print('Element not found')
                    return
            


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cdll = Cdll()
cdll.create_cdll(100)
for i in range (101,111):
    cdll.insertion(i,-1)
cdll.insertion(200,0)
cdll.insertion(100,-1)
print([node.value for node in cdll])
cdll.search(100)