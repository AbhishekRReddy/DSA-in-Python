class BinaryTree:
    def __init__(self, size):
        self.list = size * [None]
        self.max_size = size
        self.last_used_index = 0

    def __str__(self):
        if self.last_used_index == 0:
            return 'Binary Tree does not exists'
        else:
            str = f'Binary Tree of size {self.max_size} exists with elements of {self.list}'
            return str

btree = BinaryTree(10)
print(btree)
