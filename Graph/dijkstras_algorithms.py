class Edge:
    def __init__(self,start_vertex,end_vertex,weight):
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex
        self.weight = weight

class Node:
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.previous_node = None
        self.neighbours = []
        self.min_distance = float('inf')
    
    def __lt__(self,other_node):
        return self.min_distance < other_node.min_distance

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self,vertex):
        self.adj_list[vertex] = []

    def add_edge(self,vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1] = vertex2

    