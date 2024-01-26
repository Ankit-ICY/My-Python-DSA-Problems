
import heapq
from heapq import heappush, heappop

ropes = [4, 3, 2, 6]
n = 4

heapq.heapify(ropes)
cost =0 
while(len(ropes)>1):
    x = heappop(ropes)
    y = heappop(ropes)
    cost+=x+y
    heappush(ropes,x+y)

print(cost)

# from queue import PriorityQueue
# heap = PriorityQueue()


# ropes = [4, 3, 2, 6]
# n = 4
# for i in range(n):
#     heap.put(ropes[i])

# count =0 
# cost = 0
# while(count!=n-1):
#     x = heap.get()
#     count+=1
#     y = heap.get()
#     cost+=x+y
#     heap.put(x+y)

# print(cost)

# ropes = [5, 4, 2, 8]
# n = 4
# heap = []
# ropes.sort()
# for i in range(n):
#     heap.append(ropes[i])


# cost = 0
# while(len(heap)>1):
#     x = heap.pop(0)
#     y = heap.pop(0)

#     cost +=x + y
#     i = len(heap)-1
#     while(i>=0 and  heap[i]>=cost):
#         i-=1
#     heap.insert(i+1, x+y)

# print(cost)