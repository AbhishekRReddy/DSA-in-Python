class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
    
    def sssp_bfs(self,start,end):
        queue=[]
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adj_vertex in self.adj_list[node]:
                new_path = path[:]
                new_path.append(adj_vertex)
                queue.append(new_path)
    
graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')Im
graph.add_vertex('d')
graph.add_vertex('e')
graph.add_vertex('f')
graph.add_vertex('g')
graph.add_edge('a','b')
graph.add_edge('a','c')
graph.add_edge('b','d')
graph.add_edge('b','g')
graph.add_edge('c','d')
graph.add_edge('c','e')
graph.add_edge('e','f')
graph.add_edge('g','f')
graph.add_edge('d','f')

short_path = graph.sssp_bfs('a','a')
print(short_path)

