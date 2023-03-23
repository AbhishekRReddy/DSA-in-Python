class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        self.adj_list[vertex] = []

    def add_edge(self,vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1] = vertex2

    