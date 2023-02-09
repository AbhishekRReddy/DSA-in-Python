class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(value) for value in values]
        return '\n'.join(values)
    
    def isEmpty(self):
        if(self.list == []):
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return

    def pop(self):
        if self.isEmpty():
            return
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            print('stack is Empty')
            return
        return self.list[-1]
    
    def delete_stack(self):
        self.list=[]
        return

stack = Stack()
for i in range(1,11):
    stack.push(i)
    

print(stack.pop())
print('----------------------------------------------------------')
print(stack)
print('----------------------------------------------------------')
print(stack.delete_stack())
print('----------------------------------------------------------')
print(stack)