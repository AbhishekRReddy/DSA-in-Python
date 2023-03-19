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
    
    def remove_edge(self,vertex1,vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                self.adjacency_list[vertex2].remove(vertex1)
            except ValueError:
                print('No edge between the given two vertices')
                return False
        return 'Invalid vertex '
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,':',self.adjacency_list[vertex])
   
    def delete_vertex(self,vertex):
        if vertex in self.adjacency_list.keys():
            child_vertices = self.adjacency_list[vertex]
            for child_veretx in child_vertices:
                self.adjacency_list[child_veretx].remove(vertex)
            del self.adjacency_list[vertex]      
    
    def bfs(self,vertex):
        visited = [vertex]
        queue =[vertex]
        while queue:
            deq_vertex = queue.pop(0)
            print(deq_vertex)
            for adj_vertex in self.adjacency_list[deq_vertex]:
                if adj_vertex not in visited:
                    visited.append(adj_vertex)
                    queue.append(adj_vertex)
    
    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adj_vertex in self.adjacency_list[pop_vertex]:
                if adj_vertex not in visited:
                    visited.append(adj_vertex)
                    stack.append(adj_vertex)
    
                    


    
graph = Graph()
graph.add_vertex('a')
graph.add_vertex('b')
graph.add_vertex('c')
graph.add_edge('a','b')
graph.add_edge('a','c')
graph.add_vertex('d')
graph.add_edge('d','b')
graph.print_graph()
print('-------------------')    
graph.dfs('a')

