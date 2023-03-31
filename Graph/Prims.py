import heapq as pq
class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = [[] for _ in range(V)]
        self.mst = []
        self.mst_wt = 0

    def add_edge(self,s,d,w):
        self.graph[s].append([w,d])
        self.graph[d].append([w,s])

    def print_adj_list(self):
        print(self.graph)

    def prims_mst(self):
        visited = [0 for _ in range(self.V)] #Dont use 'in' operator to check the element is there in list or not.
        
        #That will leads to O(n) complexity
        heap = []
        pq.heappush(heap, [0,0,0]) #w,d,s
        #We are starting from standing 0th node.
        while len(heap) > 0:
            x = pq.heappop(heap)
            current_node = x[1]
            cuurent_weight = x[0]
            if visited[current_node] == 1: #There could be situation where multiple paths same destination
                continue
            visited[current_node] = 1
            self.mst.append(x)
            self.mst_wt += cuurent_weight
            for node in self.graph[current_node]:
                adj_node = node[1]
                adj_node_wt = node[0]
                if visited[adj_node] == 0:
                    pq.heappush(heap,[adj_node_wt,adj_node,current_node])
        print(self.mst)
        print(self.mst_wt)


g = Graph(5)
g.add_edge(0,1,2)
g.add_edge(0,2,1)
g.add_edge(2,1,1)
g.add_edge(2,3,2)
g.add_edge(2,4,2)
g.add_edge(4,3,1)
g.prims_mst()
print(g.mst)




    
