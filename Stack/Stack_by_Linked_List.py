class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        if self.head is None:
            return ' Stack is Empty'
        pointer = self.head
        values = []
        while pointer:
            values.append(str(pointer.value))
            pointer = pointer.next
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.head is None:
            return True
        return False
    
    def push(self,value):
        element = Node(value)
        element.next = self.head
        self.head = element
    
    def pop(self):
        pop_value = self.head.value
        self.head = self.head.next
        return pop_value

    def peek(self):
        if self.head is None:
            return 'Stack is Empty'
        return self.head.value

    def delete_all(self):
        self.head = None
        print('Stack has been successfully deleted')
        return



stack = Stack()
for i in range(10):
    stack.push(i)
print(stack.peek())
print('-----------------------------')
print(stack)