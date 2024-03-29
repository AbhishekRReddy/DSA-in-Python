#Let us simplify that the vertices of graph are numbers 
#Instead of the letters. This will be easier and simple to implement

class Disjoint:
    def __init__(self,no_vertices):
        self.parent = []
        self.rank = [0] * (no_vertices+1)
        self.size = [1] * (no_vertices+1)
        for i in range(no_vertices+1):
            self.parent.append(i)
    
    def find_ult_parent(self,node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_ult_parent(self.parent[node]) 
        '''Compressing the path of the tree so that we can access the parent of the node 
        in the constant time'''
        return self.parent[node]
    
    def union_by_rank(self,u, v):
        ult_u = self.find_ult_parent(u)
        ult_v = self.find_ult_parent(v)
        if ult_u == ult_v: #If both parents are same means they are in same set.
            return
        elif self.rank[ult_u] > self.rank[ult_v]:
            self.parent[ult_v] = ult_u
        elif self.rank[ult_u] < self.rank[ult_v]:
            self.parent[ult_u] = ult_v
        else:
            self.parent[ult_v] = ult_u
            self.rank[ult_u] += 1
        '''
        Why are we attacing the tree with smaller rank to larger rank?
        Becuase, we dont want to increase the rank of the of tree so that path
        taken to compute the parent during the path compression will be 
        less.
        '''
    def union_by_size(self,u,v):
        ult_u = self.find_ult_parent(u)
        ult_v = self.find_ult_parent(v)
        if ult_u == ult_v:
            return
        elif self.size[ult_u] < self.size[ult_v]:
            self.parent[ult_u] = ult_v
            self.size[ult_v] += self.size[ult_u]
        else:
            self.parent[ult_v] = ult_u
            self.size[ult_u] += self.size[ult_v]

'''ds = Disjoint(7)
ds.union_by_size(1,2)
ds.union_by_size(3,4)
ds.union_by_size(4,5)
ds.union_by_size(5,6)
ds.union_by_size(6,7)
print(ds.find_ult_parent(7))        
'''


