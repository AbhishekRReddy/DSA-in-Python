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
        
                







''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cdll = Cdll()
cdll.create_cdll(100)
for i in range (101,111):
    cdll.insertion(i,-1)
cdll.insertion(200,0)
cdll.insertion(99,11)
print([node.value for node in cdll])