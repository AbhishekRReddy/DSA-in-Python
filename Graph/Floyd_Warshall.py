import copy

def print_sol(v,graph):
    for i in range(v):
        for j in range(v):
            print(graph[i][j],end =' ')
        print(' ')


def floyd_warhall(graph):
    v = len(graph)
    dist = copy.deepcopy(graph)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
    print_sol(v,dist)
inf = float('INF')    
graph = [[0,8,inf,1],
         [inf,0,1,inf],
         [4,inf,inf,0],
         [inf,2,9,0]
]

floyd_warhall(graph)