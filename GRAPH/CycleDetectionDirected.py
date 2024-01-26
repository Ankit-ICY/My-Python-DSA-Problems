def cylceCheckDFS(adj,v , visited,dfs ,node):
    visited[node] = True
    dfs[node] = True

    for i in adj[node]:
        if not visited[i]:
            if cylceCheckDFS(adj,v , visited,dfs ,i):                
                return True

        elif dfs[i] == True:
            return True
        
    dfs[node] = False
    
    return False


adj = [[1] , [2],[] ]
v= 3
visited = {}
dfs = {}
for i in range(v):
    visited[i] = False
    dfs[i] = False

for i in range(v):
    if not visited[i] :
        if cylceCheckDFS(adj,v,visited,dfs,i ):
            print(True)
            break