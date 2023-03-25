import heapq
'''
All pair shortest path implementation with CLRS
Djikstras implementation
'''
def djikstras(graph,start):
    dist = {}
    prev = {}
    visited = []
    
    #Initializing all the nodes to the infinity and previous nodes of all the nodes as None
    for node in graph:
        dist[node] = float('inf')
        prev[node] = None
    
    #Distance of starting is setting to 0
    dist[start] = 0

    #Setting the priority queue 
    heap = [start]

    while heap:
        current_node= heapq.heappop(heap)
        #If the current node is already visited, then it will be not considered
        if current_node in visited:
            continue
        visited.append(current_node)
        #The input graph will dictionary of the dictionary
        for adj_node in graph[current_node]:
            if adj_node in visited:
                continue
            new_dist = dist[current_node] + graph[current_node][adj_node]
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                prev[adj_node] = current_node
                heapq.heappush(heap,adj_node)
    return dist, prev 

def shortest_path(graph,start,end):
    distances , prev_nodes = djikstras(graph, start)
    node = end
    path = []
    while node:
        path.append(node)
        node = prev_nodes[node]
    if path[-1] != start:
        print('Sorry the path does not exist')
        return
    print(distances)
    path.reverse()
    return path

graph = {'A' : {'B':6,'D':9,'C':10},
         'B' : {'D':5,'E':16,'F':13},
         'C' : {'D':6,'H':5,'G':21},
         'D' : {'F':8,'H':7},
         'E' : {'G':10},
         'F' : {'E':4,'G':12},
         'G' : {},
         'H':{'F':2,'G':14}
}

path = shortest_path(graph, 'A', 'F')
print(path)









