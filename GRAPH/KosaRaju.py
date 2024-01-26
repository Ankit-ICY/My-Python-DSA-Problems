def kosaraju(visited, transpose, top ):
    visited[top] = True

    for i in transpose[top]:
        if not visited[i]:
            kosaraju(visited, transpose, i )

            

def dfs(adj, visited,stack , node):
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:    
            dfs(adj, visited,stack ,i)

    stack.append(node)

    
    
edges =  [[0,1],[0,2],[1,2],[3,4],[3,5]]
n = 6
adj = [[]for _ in range(n)]
for i  in range(len(edges)):
    u = edges[i][0]
    v = edges[i][1]
    adj[u].append(v)


# adj = [[1, 0],[0 ,2],[2 ,1],[0 ,3],[3 ,4]]

if len(adj)!=n:
    l = n - len(adj)
    for i in range(l):
        adj.append([])

# TOPOLOGICAL
print(adj)

visited = [False]*n
stack = []
for i in range(n):
    if not visited[i]:
        dfs(adj, visited,stack , i)

transpose =[[] for _ in range(n)]
for  i in range(n):
    visited[i] = False
    for j in adj[i]:
        transpose[j].append(i)


count = 0

while(stack):
    top = stack.pop()
    if not visited[top]:
        count+=1
        kosaraju(visited, transpose, top )


print(count)


# while(stack):
    # top = stack.pop()
    # if not visited[top]:
    #     q = [top]
    #     count+=1
    #     while q :
    #         node = q.pop()
    #         visited[node] = True
    #         for i in transpose[node]:
    #             if not visited[i]:
    #                 q.append(i)

                


