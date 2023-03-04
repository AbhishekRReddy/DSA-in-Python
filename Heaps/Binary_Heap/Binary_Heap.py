class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.current_heap_size = 0
        self.max_heap_size = size + 1

heap = Heap(5)