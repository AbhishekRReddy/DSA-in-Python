class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = (str(value) for value in values)
        return '\n'.join(values)
    
