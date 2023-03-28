import Disjoint_Data_Structure as dst

class Graph:
    def __init__(self, no_vertices):
        self.no_vertices = no_vertices
        self.graph = [] #Contains the (Source, Destination, Weight). 
        self.MST = []
        self.mst_weight = 0
    
    def add_edge(self, s, d, w):
        self.graph.append([s,d,w])

    def print_solution (self):
        for s,d,w in self.MST:
            print(s,':',d,'-',w)

    def kruskal(self):
        ds = dst.Disjoint(self.no_vertices) #Created the set for all the individual vertices.
        self.graph = sorted(self.graph, key = lambda  item : item[2])
        #Sort based on the weight of the Graph.
        for edge in self.graph: # MST contains the number of edges = V - 1
            s, d, w = edge 
            x = ds.find_ult_parent(s) #Checking which sets does these S and D belongs.
            y = ds.find_ult_parent(d)
            if x != y: #They should not belong same set as it will form the cycle.
                self.mst_weight += w #We got one edge. 
                self.MST.append([s,d,w])
                ds.union_by_rank(x, y)
        self.print_solution()
        print(self.mst_weight)

g =Graph(6)
g.add_edge(1,4,1)
g.add_edge(4,1,1)
g.add_edge(4,2,3)
g.add_edge(5,1,4)
g.add_edge(5,4,9)
g.add_edge(4,3,5)
g.add_edge(3,2,3)
g.add_edge(3,6,8)
g.add_edge(2,6,7)
g.add_edge(1,2,2)

g.kruskal()


