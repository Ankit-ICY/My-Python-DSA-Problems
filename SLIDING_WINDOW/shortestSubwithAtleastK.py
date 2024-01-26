nums =[48,99,37,4,-31]

k = 140
sum = 0
ans = 1e9
dic = {}

heap = []
from heapq import heapify, heappop, heappush


for i in range(len(nums)):
    sum +=nums[i]
    diff = sum-k
    if diff in dic:
        ans = min( ans , i- dic[diff])
        dic[sum] = i
    else:
        dic[sum] = i


print(ans)


# i =0

# sum = 0
# ans = 1e9
# for j in range(len(nums)):

#     sum += nums[j]


#     while sum >= k:
#         ans = min(ans, j-i+1)
#         sum-=nums[i]
#         i+=1


# print(ans)