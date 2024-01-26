
edges = [[5, 2],[5, 0],[4, 0],[4, 1],[2, 3],[3, 1]]
n = 6
e = 6

adj = {}
for  i in range(e):
    u = edges[i][0]
    v = edges[i][1]
    if u in adj:
        adj[u].append(v) 
    else:
        adj[u] = [v]
    if v not in adj:
        adj[v] = []

indegree = [0]*n


for  i  in adj: 
    for j in adj[i]:
        indegree[j]+=1

    
q = []
for i in range(n):
    if indegree[i] == 0:
        q.append(i)


ans = []

while(q ):
    fnode= q.pop(0)
    ans.append(fnode)
    for i in adj[fnode]:
        indegree[i]-=1  
        if indegree[i] <= 0:
            q.append(i)

print(ans)


