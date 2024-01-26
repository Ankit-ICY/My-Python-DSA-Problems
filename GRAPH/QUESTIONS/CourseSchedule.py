def topo(node , visited,stack,adj):
    
    visited[node] = True
    dfs[node]= True
    for i in adj[node]:
        if not visited[i]:
            topo(i, visited,stack ,adj)

        if dfs[i]:
            return 
            
    dfs[node]= False
    stack.append(node)



edges = [[1,0]]
v = 2

adj = {}

adj = [[] for i in range(v)]
for i in range(len(edges)):
    adj[edges[i][1]].append(edges[i][0])


dfs = [False]*v
visited = [False]*v
stack = []

    
for i in range(v):
    if not visited[i] :
        topo(i , visited,stack ,adj)


print(stack)