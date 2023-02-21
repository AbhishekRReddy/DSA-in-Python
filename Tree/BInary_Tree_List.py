class BinaryTree:
    def __init__(self, size):
        self.list = (size+1) * [None]
        self.max_size = size+1
        self.last_used_index = 0

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



btree = BinaryTree(10)
for i in range(1,11):
    btree.insert_node(i)
print(btree)
btree.search_node(11)


