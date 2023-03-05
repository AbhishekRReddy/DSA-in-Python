class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.current_heap_size = 0
        self.max_heap_size = size + 1
    
def peek_heap(root_node):
    if root_node is None:
        return None
    return root_node.custom_list[1]

def heap_size(root_node):
    if root_node is None:
        return None
    return root_node.current_heap_size

def level_order_traversal(root_node):
    if root_node is None:
        return None
    for node in root_node.custom_list:
        print(node, end = '--')

def heapify_insert_node(root_node, index, heap_type):
    if index <= 1:
        return root_node
    parent_index = index//2
    if heap_type =='Min':
        if root_node.custom_list[index] < root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_insert_node(root_node, parent_index, heap_type)
    elif heap_type == 'Max':
        if root_node.custom_list[index] > root_node.custom_list[parent_index]:
            temp = root_node.custom_list[index]
            root_node.custom_list[index] = root_node.custom_list[parent_index]
            root_node.custom_list[parent_index] = temp
        heapify_insert_node(root_node, parent_index, heap_type)
    
def insert_node(root_node, value, heap_type):
    if root_node.current_heap_size + 1 == root_node.max_heap_size:
        print('The heap is full')
        return
    root_node.custom_list[root_node.current_heap_size + 1] = value
    root_node.current_heap_size += 1
    heapify_insert_node(root_node, root_node.current_heap_size, heap_type)
    return ' The node has been successfully implemented'
    

    



heap = Heap(10)
for i in range (10, 40, 5):
    insert_node(heap, i, 'Min')

level_order_traversal(heap)

insert_node(heap,7, 'Min')
print('-------------------------------')
level_order_traversal(heap)