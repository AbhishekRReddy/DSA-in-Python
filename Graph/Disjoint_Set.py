class DisjointSet:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            #Initializing the parent of all the vertices to itself, in the beginning.
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    #FindItem returns the main parent of set where the given node belongs.
    def find_item(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find_item(self.parent[item])
    
    def union(self,x, y):
        xroot = self.find_item(x)
        yroot = self.find_item(y)
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] +=1
        

vertices = ['A','B','C','D','E']
ds = DisjointSet(vertices)
ds.union('A','B')
print(ds.find_item('B'))
ds.union