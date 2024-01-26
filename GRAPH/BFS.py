def bfs(visited, ans,node , g):
    q = [node]
    visited[node] = True

    while(q):
        fnode = q.pop(0)
        ans.append(fnode)

        for i in g[fnode]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

        
    return ans

edges = [[4,4] , [0,1] , [0,3], [1,2], [2,3]]
v = 5
g = {}
visited= {}
for i in range(v):
    visited[i] = False
    u = edges[i][0]
    v = edges[i][1]

    if u not in g:
        g[u] = [v]
    else:
        g[u].append(v)

    if v not in g:
        g[v] = [u]
    else:
        g[v].append(u)

ans = []
for i in range(v):
    if not visited[i] :
        bfs(visited, ans,i , g)

print(ans)