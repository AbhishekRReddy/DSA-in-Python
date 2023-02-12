class CircularQueue:
    def __init__(self,maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = reversed([str(values) for value in self.items])
        return '-->'.join(values)
    
    def isFull(self):
        if (self.top+1 == self.start) or (self.start ==0 and self.top + 1 ==self.maxsize):
            return True
        else:
            return False
