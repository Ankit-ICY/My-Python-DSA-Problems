def solve(node, adj,color):
    color[node] = 0
    q = [node]

    while(q):
        vertex = q.pop(0)
        for  i in adj[vertex]:
            if color[i]==-1:
                color[i] = not color[vertex]
                q.append(i)
            elif color[i] == color[vertex]:
                return False

    return True
adj = [[1,3],[0,2],[1,3],[0,2]]
v = len(adj)
color = [-1]*v
for i in range(v):
    if color[i] == -1:
        if not solve(i , adj,color):
            print(False)    
            break
        
print(color)