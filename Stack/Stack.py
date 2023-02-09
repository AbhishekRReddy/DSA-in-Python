class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = (str(value) for value in values)
        return '\n'.join(values)
    
    def isEmpty(self):
        if(self.list == []):
            return True
        else:
            return False
stack = Stack()
print(stack.isEmpty())