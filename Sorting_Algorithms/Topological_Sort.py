from collections import defaultdict
class Graph:
    def __init__(self,no_vertices):
        self.graph = defaultdict(list)
        self.no_vertices = no_vertices
    
    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
    
    def topological_sort_list(self,v, visited, stack):
        visited.append(v)
        for adj_vertex in self.graph[v]:
            if adj_vertex not in visited:
                self.topological_sort_list(adj_vertex, visited, stack)
        stack.insert(0, v)
    
    def topological_sort(self):
        visited = []
        stack = []
        for vertex in self.graph.keys():
            if vertex not in visited:
                self.topological_sort_list(vertex, visited, stack)
        print(stack)

my_graph = Graph(8)
my_graph.add_edge('a','c')
my_graph.add_edge('b','c')
my_graph.add_edge('b','d')
my_graph.add_edge('c','e')
my_graph.add_edge('d','f')
my_graph.add_edge('e','h')
my_graph.add_edge('e','f')
my_graph.add_edge('f','g')
my_graph.graph['h']
my_graph.graph['g']
print(my_graph.graph)
my_graph.topological_sort()
