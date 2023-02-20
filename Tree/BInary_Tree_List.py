class BinaryTree:
    def __init__(self, size):
        self.list = (size) * [None]
        self.max_size = size
        self.last_used_index = 0

    def __str__(self):
        if self.last_used_index == 0:
            return 'Binary Tree does not exists'
        else:
            str = f'Binary Tree of size {self.max_size} exists with elements of {self.list}'
            return str

    def insert_node(self, value):
        if self.last_used_index + 1 == self.max_size:
            print('Binary Tree is Full')
            return
        self.list[self.last_used_index+1] = value
        self.last_used_index += 1


btree = BinaryTree(10)
for i in range(1,10):
    btree.insert_node(i)
print(btree)


