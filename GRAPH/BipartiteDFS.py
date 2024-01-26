def solve(node , color , adj, col ):
    color[node] = col
    for  i in adj[node]:
        if color[i] == -1:
            if  solve(i , color , adj, not col ) == False:
                return False
        elif color[i] == col:
            return False



    return True

adj =[[1,3],[0,2],[1,3],[0,2]]
v = len(adj)
color = [-1]*v


for i in range(v):
    if color[i] == -1:
        if not solve(i , color , adj , 0):
            print(False)
            break