def solve(visited , adj,node):
    visited[node] = True

    for i in adj[node]:
        if not visited[i]:
            solve(visited , adj,i)



isConnected =[[1,1,0],[1,1,0],[0,0,1]]
            
n = len(isConnected[0])

adj = [[] for _ in range(n+1)]

for i in range(n):
    for j in range(n):
        if isConnected[i][j] == 1:
            adj[i+1].append(j+1)


visited = [False]*(n+1)
count = 0
for i in range(1, n+1):
    if not visited[i]:
        solve(visited , adj,i)
        count+=1


print(count)