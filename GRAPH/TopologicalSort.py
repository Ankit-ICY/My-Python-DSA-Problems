def topo(node , visited,stack,adj):
    
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            topo(i, visited,stack ,adj)
            
    stack.append(node)


            
        
adj = [[3,4],[3,0],[1,0],[2,0] ,[]]
v = 5
visited = {}
stack = []
for i in range(v):
    visited[i] = False
    
for i in range(v):
    if not visited[i] :
        topo(i , visited,stack ,adj)
 

stack.reverse()

print(stack)