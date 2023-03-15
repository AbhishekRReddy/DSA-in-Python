class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self,vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
        
    def add_edge(self,vertex,edge):
        self.adjacency_list[vertex].append(edge)
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,':',self.adjacency_list[vertex])
    


dict = {'a':['b','c'],
        'b':['d','e',],
        'c':['e'],
        'd':['e','f'],
        'f':['d','e']
}
graph = Graph()
graph.add_vertex('a')
graph.add_edge('a','b')
graph.add_edge('a','c')
graph.print_graph()