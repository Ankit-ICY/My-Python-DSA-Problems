def solve(visited, dfs, adj , node,ans):

    visited[node] = True
    dfs[node] = True

    for i in adj[node]:
        if not visited[i]:
            solve(visited, dfs, adj , i,ans)

        if dfs[i]:
            return 
        

    dfs[node] = False
    ans.append(node)

    return ans

adj = [[1,2,3,4],[1,2],[3,4],[0,4],[]]

n = len(adj)

visited = [False]*n
dfs = [False]*n


ans = []
for i in range(n):
    if not visited[i]:
        solve(visited, dfs, adj , i ,ans)


print(ans)