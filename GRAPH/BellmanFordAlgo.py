edges = [[0,1,5],[1,0,3],[1,2,-1],[2,0,1]]
s = 2
v = 3
e = len(edges)
distance = [1e9]*v
distance[s] = 0

adj  = {}
for i in range(4):  
    u = edges[i][0]
    x = edges[i][1]
    w = edges[i][2]

    if u not in adj:
        adj[u] = [[x,w]]

    else:
        adj[u].append([x,w])
    
for i in range(v):
    if i not in adj:
        adj[i] = []

print(adj)
for i in range(v-1):
    
    q = [s]
    while q:
        node = q.pop(0)
        for n in adj[node]:
            nodeDistance = n[1]
            vertex = n[0]

            if nodeDistance + distance[node] < distance[vertex]:
                distance[vertex] = nodeDistance + distance[node]
                q.append(vertex)


print(distance)