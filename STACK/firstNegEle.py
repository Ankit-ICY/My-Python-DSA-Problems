nums = [12, -1, -7, 8, -15, 30, 16, 28]
n = len(nums)
k  = 3
from collections import deque
dq = deque()
for i in range(k):
    if  nums[i] <0:
        dq.append(i)
    


ans = []
ans.append(nums[dq[0]])
for  i in range(k,n):

    # REMOVAL
    while dq and i - dq[0] >= k:
        dq.popleft()


    
    if  nums[i] <0:
        dq.append(i)
    
    if dq:
        ans.append(nums[dq[0]])

    else:
        ans.append(0)


  
print(ans)
