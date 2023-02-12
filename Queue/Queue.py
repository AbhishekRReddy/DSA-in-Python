class Queue:
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        values = reversed([str(value) for value in self.queue])
        return '-->'.join(values)
    
    def isEmpty(self):
        if self.queue == []:
            return True
        return False
    
    def enqueue(self,value):
        self.queue.append(value)
        return 'Successfully enqueued'
    
    def dequeue(self):
        if self.queue == []:
            return 'Queue is empty'
        self.queue.pop(0)
        return
    
custom_queue = Queue()
for i in range(1,5):
    custom_queue.enqueue(i)
#`custom_queue.dequeue()
print(custom_queue)