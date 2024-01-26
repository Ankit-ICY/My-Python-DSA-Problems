nums = [100 ,80 ,60 ,70 ,60, 75 ,85]
n = len(nums)
stack = []
ans = [1]*n

for i in range(n):
    while(stack and nums[i]>stack[-1]):
        ans[i]+=1
        stack.pop()
        
        
    stack.append(nums[i])


print(ans)