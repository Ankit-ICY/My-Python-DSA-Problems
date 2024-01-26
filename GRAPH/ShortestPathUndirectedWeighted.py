def solve(vertex , parent, distance, adj , visited):
    distance[vertex] = 0 
    q = [vertex]
    while (q):
        node = q.pop(0)
        for i in adj[node]:
            nodeDistance =  i[1]  
            nb = i[0]

            if not visited[nb]:
                visited[nb] = True
                parent[nb] = node
                distance[nb] = nodeDistance + distance[node]
                q.append(nb)
          
            elif nodeDistance + distance[node] < distance[nb] :
                distance[nb] = nodeDistance + distance[node]
                parent[nb] = node
                q.append(nb)        

edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
n = 5
e = 6
adj = {}
for i in range(e):
    u = edges[i][0]
    v = edges[i][1]
    w = edges[i][2]
    if u in adj:
        adj[u].append([v,w])
    else:
        adj[u] = [[v,w]]

    if v in adj:
        adj[v].append([u,w])
    else:
        adj[v] = [[u,w]]

parent = [-1]*(n +1)

distance = [1e9] *(n+1)
visited = [False] * (n+1)
solve(1 , parent, distance, adj , visited)
print(distance)

print(parent)
currentNode = n
ans = []
ans.append(currentNode)
while currentNode != 1:
    currentNode = parent[currentNode]
    ans.append(currentNode)

ans.reverse()
print(ans)
