import Disjoint_Set as dst

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [] #Contains the (Source, Destination, Weight). 
        self.nodes = []
        self.MST = []
    
    def add_edge(self, s, d, w):
        self.graph.append([s,d,w])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution (self,s,d,w):
        for s,d,w in self.MST:
            print(s,':',d,'-',w)

    def kruskal(self):
        i, e = 0,0
        ds = dst.DisjointSet(self.nodes) #Created the set for all the individual vertices.
        self.graph = sorted(self.graph, key = lambda  item : item[2])
        #Sort based on the weight of the Graph.
        while e < self.V: # MST contains the number of edges = V - 1
            s, d, w = self.graph[i]
            i += 1
            x = ds.find_item(s) #Checking which sets does these S and D belongs.
            y = ds.find_item(d)
            if x != y: #They should not belong same set as it will form the cycle.
                e += 1 #We got one edge. 
                self.MST.append([s,d,w])
                ds.union(x, y)
        self.print_solution(s,d,w)


         

    
