def BridgeCheck(adj,node,visited, parent,disc, timer,low):


    low[node] = timer[0]    
    disc[node] = timer[0]
    visited[node] = True
    timer[0] = timer[0] + 1
    for child  in adj[node]:
        if not visited[child]:
            BridgeCheck(adj,child,visited, node,disc, timer,low)
            low[node] = min(low[node] , low[child] )
            
            if low[child]> disc[node]:
                ans = []
                ans.append(node)
                ans.append(child)
                result.append(ans.copy())


        elif child==parent:
            continue

        else:
            # BACK EDGE
            low[node] = min(low[node] , disc[child])



# ,[3 ,3],[0 ,1],[1, 2],[2 ,0]
edges = [[0 ,1], [3 ,1],[1 ,2],[3 ,4]]  
adj = {}
e = 4
for  i in range(e):
    u = edges[i][0]
    v = edges[i][1]
    if u in adj:
        adj[u].append(v) 
    else:
        adj[u] = [v]
    if v not in adj:
        adj[v] = [u]
    else:
        adj[v].append(u)


v = 5
low = [-1]*v
visited = [False]*v
parent = -1
disc = [-1] *v
timer = [0]
ans = []
result = []
for i in range(v):
    if not visited[i]:
        BridgeCheck(adj,i,visited, parent,disc, timer,low)


print(result)