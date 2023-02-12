class CircularQueue:
    def __init__(self,maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        if self.start == -1:
            return 'Queue is empty'
         
        values = reversed([str(value) for value in self.items])
        return '-->'.join(values)
    
    def isFull(self):
        if (self.top+1 == self.start) or (self.start == 0 and self.top + 1 ==self.maxsize):
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top ==-1:
            return True
        return False
    
    def enqueue(self,value):
        if self.isFull():
            return 'Queue is empty'
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return 'Enqueue has been successfully completed'
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is Empty'
        else:
            firstElem = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxsize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElem
    
    def peek(self):
        if self.start ==-1:
            return 'Queue is Empty'
        else:
            return self.items[self.start]
    def delete_all(self):
        self.items= self.maxsize * [None]
        self.start = -1
        self.top = -1
        print('Queue is successfully deleted')




    

customQueue = CircularQueue(6)
for i in range(0,6):
    customQueue.enqueue(i)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
customQueue.enqueue(99)
print(customQueue.dequeue())
print(customQueue)
print(customQueue.peek())
customQueue.delete_all()
print(customQueue)
