class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
        
    def add_edge(self,vertex1,veretx2):
        if vertex1 in self.adjacency_list.keys() and veretx2 in self.adjacency_list.keys():   
            self.adjacency_list[vertex1].append(veretx2)
            self.adjacency_list[veretx2].append(vertex1)
            return True
        return 'Invalid vertex  '
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,':',self.adjacency_list[vertex])
    
graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_edge('a','b')
graph.add_edge('a','c')
graph.print_graph()