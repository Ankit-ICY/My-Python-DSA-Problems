# tasks = ["A","A","A","B","B","B", "C","C","C", "D", "D", "E"]
tasks = ["A","B","A"]
tasks.sort()
n = 2
from heapq import heapify , heappop, heappush
heap = []
count = 1
for i in range( len(tasks)-1):
    if tasks[i] == tasks[i+1]:
        count+=1
    else:
        heappush(heap , [-count, tasks[i]])
        count = 1


heappush(heap,[-count, tasks[-1]])

    
ans= 0 
store = []
count=0
while heap or store:
    cell = heappop(heap)
    count+=1
    cell[0]+=1
    ans+=1
    if cell[0]<0:
        store.append(cell)
    
    if count == n+1:
        count = 0
        while store:
            heappush(heap, store.pop())

    if not heap and store:
        if count<n+1 :
            ans+= (n+1)-count
            count = 0
            while store:
                heappush(heap, store.pop())
            

print(ans)