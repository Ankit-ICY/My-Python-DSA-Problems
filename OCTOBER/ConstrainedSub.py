# def solve(nums,k,dp,ind,prev):

#     if ind>=len(nums):
#         return 0

#     sol = 0
#     if prev == -1 or  ind-prev <=k:
#         take = nums[ind] +   solve(nums,k,dp,ind+1,ind)
#         nottake = solve(nums,k,dp,ind+1,prev)
#         sol = max(take, nottake)

#     return sol

 

# nums = [-1,-2,-3]
# k = 1
# dp ={}
# ind = 0
# print(solve(nums,k,dp,ind,-1))


#  HEAP APPOACH



nums = [10,2,-10,5,20]
k = 2
ans = nums[0]

from heapq import heapify ,heappop, heappush
heap = [(-nums[0] , 0)]


for i in range(1,len(nums)):
    while i - heap[0][1] > k:
        heappop(heap)


    maxi = max( nums[i], nums[i] - heap[0][0]  )
    ans = max(ans, maxi)
    heappush(heap , (-maxi ,i))

print(ans)














