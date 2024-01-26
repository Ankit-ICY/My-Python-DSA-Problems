def getShortestPath(stack , adj , src ,distance):
    distance[src] = 0
    while(stack):
        top = stack.pop()
        # if distance[top] != 1e9:
        for i in adj[top]:
            if distance[top] + i[1] < distance[i[0]]:
                distance[i[0]] = distance[top] + i[1]



def TopoSort(adj, node , visited,stack):
    visited[node] = True
    for i in adj[node]:
        if not visited[i[0]] :
            TopoSort(adj, i[0] , visited,stack)

    stack.append(node)


edge =[[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
e = 7
n = 6

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
        adj[v] = []


distance=  []
for i in range(n):
    distance.append(1e9)
visited = [False] * n
stack = []
for i in range(n):
    if not visited[i]:
        TopoSort(adj, i , visited,stack)


src = 0
getShortestPath(stack , adj , src ,distance)

print(distance)