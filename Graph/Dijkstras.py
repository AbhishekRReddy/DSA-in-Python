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
    
    def add_edge(self, other_node,weight):
        self.neighbours.append(Edge(self,other_node,weight))
        
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
                start = edge.start_vertex
                end = edge.end_vertex
                new_distance = start.min_distance + edge.weight
                if end.min_distance > new_distance:
                    end.min_distance = new_distance
                    end.previous_node = start
                    heapq.heappush(self.heap, end)
            actual_vertex.visited = True

    def get_shortest_path(self,vertex):
        print(f'The minimum distance to the given vertex {vertex.min_distance}')
        temp = []
        while vertex:
            temp.insert(0,vertex.name)  
            vertex = vertex.previous_node
        print(temp)


nodeA = Node('A')
nodeB = Node('B')
nodeC= Node('C')    
nodeD = Node('D')
nodeE = Node('E')
nodeF = Node('F')
nodeG = Node('G')
nodeH = Node('H')
nodeA.add_edge(nodeB,6)
nodeA.add_edge(nodeD,9)
nodeA.add_edge(nodeC,10)
nodeB.add_edge(nodeD,5)
nodeB.add_edge(nodeE,16)
nodeB.add_edge(nodeF,13)
nodeC.add_edge(nodeD,6)
nodeC.add_edge(nodeH,5)
nodeC.add_edge(nodeG,21)
nodeD.add_edge(nodeF,8)
nodeD.add_edge(nodeH,7)
nodeE.add_edge(nodeG,10)
nodeF.add_edge(nodeE,4)
nodeF.add_edge(nodeG,12)
nodeH.add_edge(nodeF,2)
nodeH.add_edge(nodeF,14)

algo =dijkstra()
algo.calculate_distance(nodeA)
algo.get_shortest_path(nodeF)
