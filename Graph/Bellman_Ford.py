class Graph:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = []
        self.nodes = []
    
    def add_edge(self,s,d,w):
        self.graph.append([s,d,w])
    
    def add_node(self,value):
        self.nodes.append(value)

    def print_solution (self, dist,src):
        for k,v in dist.items():
            print(f'The Minimum distance from {src} to the vertex {k} is {v}')
    def bellman_ford(self,src):
        dist = {i : float('inf') for i in self.nodes}
        dist[src] = 0
        for _ in range(self.v-1):
            for s,d,w in self.graph:
                if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w

        for s,d,w in self.graph:
            if dist[s] != float('inf') and dist[s] + w < dist[d]:
                    return 'Negative cycle exists in the given graph'
        self.print_solution(dist,src)
    
g = Graph(5)
g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('E')
g.add_edge('A','B',4)
g.add_edge('A','C',2)
g.add_edge('B','C',3)
g.add_edge('B','D',2)
g.add_edge('B','E',3)
g.add_edge('C','B',1)
g.add_edge('C','E',5)
g.add_edge('C','D',4)
g.add_edge('E','D',-5)

g.bellman_ford('A')