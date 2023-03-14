class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            self.gdict = {}
        else:
            self.gdict = gdict
    
    def add_edge(self,vertex,edge):
        self.gdict[vertex].append(edge)

dict = {'a':['b','c'],
        'b':['d','e',],
        'c':['e'],
        'd':['e','f'],
        'f':['d','e']
}
graph = Graph(dict)
graph.add_edge('a','d')
print(graph.gdict)