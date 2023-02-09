class Stack:
    def __init__(self,maxValue):
        self.maxValue = maxValue
        self.list = []
    
    def __str__(self):
        values = reversed(self.list)
        values = [str(value) for value in values]
        return '\n'.join(values)
        
    
    def isEmpty(self):
        if self.list == []:
            return True
        return False
    def isFull(self):
        if len(self.list) == self.maxValue:
            return True
        return False

    def push(self, value):
        if self.isFull():
            print('Stack is already full')
            return
        self.list.append(value)
        

    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        return self.list[-1]

    def delete_stack(self):
        self.list = []
        print('Stack is deleted')
        return



stack = Stack(10)
for i in range(15):
    stack.push(i)
print(stack)
print('@@@@@@@@@@@@@@@@@@')
print()