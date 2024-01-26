nums =  [11,81,94,43,3]
n = len(nums)
left = [-1]*n
right = [0] *n
stack = []
for i in range(n):
    while stack and nums[stack[-1]] >= nums[i]:
        stack.pop()

    if stack:
        left[i] =  stack[-1]

    stack.append(i)

stack.clear()
for i in range(n-1, -1, -1):
    while stack and nums[stack[-1]] > nums[i]:
        stack.pop()

    if stack:
        right[i] =  stack[-1] 
    else:
        right[i] =  n 

    stack.append(i)

print(left)
print(right)

ans = 0
for i in range(n):
    ans +=  nums[i] * ( i - left[i]) * (right[i]-i )

print(ans)