edge = [[0 ,1 ,6] , [ 1 ,3 ,9], [0 ,2, 3] , [0, 3, 1] , [2,3,6]]
e = 5
adj = {}
for i in range(e):
    u = edge[i][0]
    v = edge[i][1]
    w = edge[i][2]

    if u not in adj:
        adj[u] = [[v,w]]
    else:
        adj[u].append([v,w])

    if v not in adj:
        adj[v] = [[u,w]]
    else:
        adj[v].append([u,w])


v = 4
mst = [False]*v
key = [1e9]*v
parent = [-1]*v



key[0] = 0
for j in range(v):
    mini = 1e9


    for i in  range(v):
        if not mst[i] and key[i] < mini:
            mini = key[i] 
            node = i

    mst[node]=  True

    for i in adj[node]:
        u = i[0]
        weight = i[1]
        
        if key[u] > weight and mst[u] == False:
            parent[u] = node 
            key[u] = weight


print(key)