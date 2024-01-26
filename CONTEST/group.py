nums =  [1,2,5]
from heapq import heapify , heappop, heappush
heap = [(-num, i) for i, num in enumerate(nums)]
heapify(heap)
ans = 0
maxi = 0
store = []
i= 0

count = 0
while heap and i<len(nums): 
    check = heappop(heap)
    check = (check[0] + 1, check[1])

    if check[0] < 0:
        store.append(check)
    count += 1

    if count > maxi:
        ans += 1
        maxi = count
        while store:
            heappush(heap, store.pop())
        i+=1
        count = 0
        store.clear()
            

   

print(ans)