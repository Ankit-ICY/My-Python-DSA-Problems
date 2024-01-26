nums = [3,2,1,5,6,4]
k = 2


from heapq import heappop,heappush,heapify
heap = []
heapify(heap)

for i in range(k):
    heappush(heap, nums[i])

print(heap)

for i in range(k,len(nums) ):
    if nums[i] > heap[0]:
        heappop(heap)
        heappush(heap, nums[i])
        

print(heap[0])