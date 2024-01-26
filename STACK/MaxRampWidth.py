nums = [6,0,8,2,1,5]
n = len(nums)    
stack = []
for i in range(n):
    if not stack or nums[stack[-1]]> nums[i]:
        stack.append(i)

best = 0
for i in range(n-1,-1,-1):
    while stack and nums[stack[-1]] <= nums[i]:
        best = max(best , i- stack.pop() )

print(best)