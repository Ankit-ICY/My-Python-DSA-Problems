exp = 16
req = [62 , 56,29,82,59,89,16,16 ]
gain = [77,73,99,10,37,46,53,68]
k = 4
n = len(req)
from heapq import heapify , heappush , heappop
heap = []
for i in range(n):
    heappush(heap, [-gain[i] , req[i]])
    
    
store = []

flag = 0

while heap and k:

    value = heappop(heap)
    if value[1] <=exp:
        exp = exp +   (-value[0])
        k-=1
        while store:
            heappush(heap, store.pop())

    else:
        store.append(value)
                    
                

print(exp)
