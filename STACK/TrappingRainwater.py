nums   =  [4,2,0,3,2,5]
stack  =  []
n =   len(nums)
left  =  [-1]*n
right =  [-1]*n
for i in range(n):
    while stack and stack[-1] < nums[i]:
        stack.pop()
    
    if stack :
        left[i] = stack[-1]
    
    if not stack:
        
        stack.append(nums[i])


stack.clear()

for i in range(n-1,-1,-1):
    while stack and stack[-1] < nums[i]:
        stack.pop()

    
    if stack :
        right[i] = stack[-1]
    
    if not stack:
        stack.append(nums[i])


ans = 0
mini = 0
for i in range(n):
    if left[i]!= -1 and right[i]!=-1:
        mini = min(left[i] , right[i])
        ans += mini - nums[i]

print(ans)