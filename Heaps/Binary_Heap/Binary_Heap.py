class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.current_heap_size = 0
        self.max_heap_size = size + 1

def peek_heap(root_node):
    if root_node is None:
        return None
    return root_node.custom_list[1]


heap = Heap(5)