class Queue:
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        values = [str(value) for value in values]
        return '<--'.join(values)
    
    def isEmpty(self):
        if self.queue == []:
            return True
        return False
    
    def enqueue(self,value):
        self.queue.append(value)
        return 'Successfully enqueued'
    