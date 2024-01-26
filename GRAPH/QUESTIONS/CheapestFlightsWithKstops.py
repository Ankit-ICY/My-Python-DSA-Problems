flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
src = 0
dst = 3
n = 4
k = 1
adj ={}
adj = [[] for _ in range(n)]
for i in range(len(flights)):
    u = flights[i][0]
    v = flights[i][1]
    w = flights[i][2]
    adj[u].append([v,w])
distance = [1e9]*n
distance[src] = 0
q = [[0, [src , 0 ]]]

while(q):
    node = q.pop(0)
    stops = node[0]
    vertex = node[1][0]
    dist = node[1][1]

    if stops>k:continue
    for i in adj[vertex]:
        v = i[0]
        w = i[1]
        if dist + w < distance[v] and stops <=k:
            distance[v] = dist + w 
            q.append([stops+1 , [v , distance[v]]])


print(distance[dst])