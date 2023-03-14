class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def add_edge(self,vertex,edge):
        self.gdict[vertex].append(edge)

    def add_vertex(self,vertex):
        self.gdict[vertex] = []

dict = {'a':['b','c'],
        'b':['d','e',],
        'c':['e'],
        'd':['e','f'],
        'f':['d','e']
}
graph = Graph(dict)
graph.add_edge('a','d')
graph.add_vertex('z')
graph.add_edge('z','g')
print(graph.gdict)