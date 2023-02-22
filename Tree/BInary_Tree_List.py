class BinaryTree:
    def __init__(self, size):
        self.list = (size) * [None]
        self.max_size = size
        self.last_used_index = 0
        self.empty_list = []

    def __str__(self):
        if self.last_used_index == 0:
            return 'Binary Tree does not exists'
        else:
            str = f'Binary Tree of size {self.max_size-1} exists with elements of {self.list}'
            return str

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            print('Binary Tree is Full')
            return
        self.list[self.last_used_index+1] = value
        self.last_used_index += 1
    
    def search_node(self, value):
        for node_value in self.list:
            if(value == node_value):
                print('Value has been found')
                return
        print('Value does not found in BT')
        return
    
    def core_pre_order_traversal(self, index = 1):
        if index > self.last_used_index:
            return
        self.empty_list.append((self.list[index]))
        self.core_pre_order_traversal(index*2)
        self.core_pre_order_traversal(index*2+1)
    
    def pre_order_traversal(self):
        self.core_pre_order_traversal()
        temp = self.empty_list[:]
        self.empty_list = []
        return temp

    def in_order_traverse(self, index = 1):
        if index > self.last_used_index:
            return
        self.in_order_traverse(index*2)
        print(self.list[index])
        self.in_order_traverse(index*2+1)
    
        




btree = BinaryTree(10)
for i in range(1,11):
    btree.insert_node(i)

btree.in_order_traverse()


