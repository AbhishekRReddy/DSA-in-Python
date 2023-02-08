class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class Cdll:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        pointer = self.head
        while pointer:
            yield pointer
            pointer = pointer.next
            if pointer == self.head:
                return

    def create_cdll(self,value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.next = node
        node.prev = node





''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
cdll = Cdll()
cdll.create_cdll(0)
print([node.value for node in cdll])