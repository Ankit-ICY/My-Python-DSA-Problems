def solve(node , visited):


    for  i in adj[node]:
        if not visited[i]:
            visited[i] = True
            solve(i , visited)


n = 4
roads =  [[1 ,1, 1 ,0 ]
         ,[1 ,1 ,1 ,0 ]
         ,[1, 1, 1 ,0 ]
         ,[0, 0 ,0 ,1 ]]


adj = [[] for _ in range(n+1)]

for i in range(1,len(roads)+1):
    for j in range(1,len(roads[0])+1):
        if i!=j and roads[i-1][j-1]:
            adj[i].append(j)
            

visited = [False]*(n+1)
count = 0
for i in range(1,n+1):
    if not visited[i]:
        visited[i] = True
        count+=1
        solve(i , visited)

print(count)