edges = [[1,2,2], [2,5,5], [2,3,4], [1,4,1],[4,3,3],[3,5,1]]
n = 5
e = 6
adj = {}
for i in range(e):
    u = edges[i][0]
    v = edges[i][1]

    if u in adj:
        adj[u].append(v)
    else:
        adj[u] = [v]

    if v in adj:
        adj[v].append(u)
    else:
        adj[v] = [u]

print(adj)
visited = [False]*(n + 1)
parent = [-1]*(n +1)

q = [1]
visited[1]  = True
while(q):
    fnode = q.pop(0)
    
    for i in adj[fnode]:
        if not visited[i]:
            visited[i] = True
            parent[i] = fnode
            q.append(i)

print(parent)
currentNode=  n
ans = []
ans.append(currentNode)
while(currentNode != 1 ):
    currentNode = parent[currentNode]
    ans.append(currentNode)

ans.reverse()
print(ans)
