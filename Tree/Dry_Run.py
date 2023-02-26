    def level_order_traversal(self):
        if self.root is None:
            return 'The BST is empty'
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.isEmpty():
            node = queue.dequeue()
            print(node.value.data)
            if node.value.left_node:
                queue.enqueue(node.value.left_node)
            else:
                queue.enqueue(node.value.right_node)

