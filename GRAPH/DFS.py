def dfs(adj , node,v , visited, ans):

    if node>=v:
        return  

    ans.append(node)
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            dfs(adj , i,v , visited, ans)

    return ans


adj = [[1,3], [2,0], [1], [0]]
node = 0
v = 4
visited ={}
for i in range(v):
    visited[i] = False
ans = []
dfs(adj , node,v, visited,ans)
print(ans)