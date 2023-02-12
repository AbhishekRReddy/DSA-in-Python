class Queue:
    def __init__(self):
        self.queue = []
    
    def __str__(self):
        values = [str(value) for value in values]
        return '-->'.join(values)
    