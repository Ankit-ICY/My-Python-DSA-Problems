nums = [1,3,1,2,0,5]
k = 3

from collections import deque

maxi = deque()

for i in range(k):
    while maxi and nums[maxi[-1]] <= nums[i]:
        maxi.pop()

    maxi.append(i)

ans = []
for i in range(k ,len(nums)):
    ans.append(nums[maxi[0]])

    # removal 

    while maxi and i - maxi[0] >= k:
        maxi.popleft()


    # ADDITION
    while maxi and nums[maxi[-1]] <= nums[i]:
        maxi.pop()

    maxi.append(i)


ans.append(nums[maxi[0]])

print(ans)
    
