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

    def enqueue(self, value):
        node = Node(value)
        if self.queue.head is None:
            self.queue.head = node
            self.queue.tail = node
            return
        else:
            node.next = self.queue.head
            self.queue.head = node
            return

myQueue = Queue()
for i in range(1,6):
    myQueue.enqueue(i)
print(myQueue)
    