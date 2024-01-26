roads = [ [1 ,3 ,2], [6 ,2 ,34]]
adj  = {}
n = 9
for i in range(len(roads)):
    u = roads[i][0]
    v = roads[i][1]
    w = roads[i][2]

    if u not in adj:
        adj[u] = [[v,w]]

    else:
        adj[u].append([v,w])

    if v not in adj:
        adj[v] = [[u,w]]
    else:
        adj[v].append([u,w])

for i in range(n):
    if i not in adj:
        adj[i] = []

from heapq import heapify, heappop, heappush

ways = [0]*n
distance = [1e9]*n
distance[0] = 0
ways[0]= 1
heap = []

heap= [ [0,0] ]

while(heap):
    node = heappop(heap)
    dist = node[0]
    v = node[1]
    for i in adj[v]:
        vertex = i[0]
        weight =  i[1]

        if weight + dist < distance[vertex]:
            distance[vertex] = weight + dist
            heappush(heap , [distance[vertex] , vertex])
            ways[vertex] = ways[v]

        elif weight + dist == distance[vertex]:
            ways[vertex] = ways[v] + ways[vertex]


print(ways)
                

# 9 2
# 1 3 2
# 6 2 34