heap  = []
from heapq import heapify , heappush , heappop
adj = [[[1, 1], [2, 6]]
       , [[2, 3], [0, 1]]
       , [[1, 3], [0, 6]]]


v = 3
s=  2

distance = [1e9]*v

heap.append([0 , s])
distance[s] = 0

while(heap):
    top = heappop(heap) 
    nodeDistance = top[0]
    node= top[1]


    for i in adj[node]:
        if i[1] + nodeDistance  < distance[i[0]]:

            if [distance[i[0]] , i[0]] in heap:
                heap.remove([distance[i[0]] , i[0]])

            distance[i[0]] =  i[1] + nodeDistance

            heappush(heap,[distance[i[0]] , i[0]] )



print(distance)