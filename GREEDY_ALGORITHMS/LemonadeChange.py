bills =[5,5,5,10,5,20,5,10,5,20]


import heapq
from heapq import heappush, heappop

heapq.heapify(bills)

store =[]

for i in range(len(bills)):
    if bills[i]== 5:
        heappush(store, 5)

    else:
        x = bills[i]
        j = len(store)-1
        while(x!=5 and len(store)>0):
            if j>=0 and store[j]<x:
                x-=store[j]
                store.pop(j)
            j-=1
            

        if x!=5:
            print(False)
            break
        store.append(bills[i])

print(store)
        




