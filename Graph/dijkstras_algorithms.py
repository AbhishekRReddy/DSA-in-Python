import heapq
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

class dijkstra:
    def __init__(self):
        self.heap = []
    
    def calculate_distance(self,start_vertex):
        start_vertex.min_distance = 0
        heapq.heappush(self.heap, start_vertex)
        while self.heap:
            actual_vertex = heapq.heappop(self.heap)
            if actual_vertex.visited:
                continue
            for edge in actual_vertex.neighbours:
                start = edge.start_vetex
                end = edge.end_vertex
                new_distance = start.min_distance + edge.weight
                if end.min_distance > new_distance:
                    end.min_distance = new_distance
                    end.previous_node = start
                    heapq.heappush(self.heap, end)
            actual_vertex.visited = True

        