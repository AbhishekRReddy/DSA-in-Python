class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer.value
            pointer = pointer.next
    
class Queue:
    def __init__(self):
        self.queue = LinkedList()
    
    def __str__(self):
        values = [str(node) for node in self.queue]
        return '<--'.join(values)

    def isEmpty(self):
        if (self.queue.head is None):
            return True
        return False

    def enqueue(self, value):
        node = Node(value)
        if self.isEmpty():
            self.queue.head = node
            self.queue.tail = node
            return
        else:
            self.queue.tail.next = node
            self.queue.tail = node
            return
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        else:
            tempNode = self.queue.head
            if self.queue.head == self.queue.tail:
                self.queue.head = None
                self.queue.tail = None
                return tempNode
            else:
                self.queue.head = self.queue.head.next
                return tempNode
    def peek(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue.head.value

    def delete_all(self):
        self.head =None
        self.tail = None




myQueue = Queue()
for i in range(1,6):
    myQueue.enqueue(i)
print(myQueue)
print(myQueue.dequeue())
print(myQueue)
print(myQueue.peek())
print(myQueue)
