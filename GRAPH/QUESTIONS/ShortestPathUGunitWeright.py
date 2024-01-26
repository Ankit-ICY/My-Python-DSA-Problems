edges=[[0,1],[0,3],[3,4],[4 ,5]
,[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]] 
src = 0
n  = 9
m = 10

adj = [[] for  _ in range(n)]
for i in range(m):
    u = edges[i][0]
    v = edges[i][1]
    adj[u].append(v)
    adj[v].append(u)

visited = [False]*n
distance = [1e9]*n
distance[src] = 0
from heapq import heapify , heappop, heappush
heap = [ [0,src] ]
heapify(heap)

while heap:
    node = heappop(heap)
    dist = node[0]
    vertex = node[1]

    for i in adj[vertex]:
        if dist + 1 < distance[i]:
            distance[i] = dist + 1
            heappush(heap ,[distance[i] , i])

print(distance)


