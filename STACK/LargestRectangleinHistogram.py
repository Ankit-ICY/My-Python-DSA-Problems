nums = [2,1,5,6,2,3,1]
n = len(nums)
left = [None]*n
right = [None]*n
stack = []
# LEFT SMALLER

for i in range(n):
    if len(stack)==0:
        left[i] = i
        stack.append(i)
        continue

    if stack and  nums[i]<=nums[stack[-1]]:
        while(stack and nums[i]<=nums[stack[-1]]):
            stack.pop()

        if len(stack)>0:
            left[i] = stack[-1]+1
        else:
            left[i] = 0

    else:
        left[i] = i
        
    stack.append(i)

# RIGHT SMALLER
stack = []
for i in range(n-1 , -1 ,-1):
    if len(stack)==0:
        right[i] = i
        stack.append(i)
        continue

    if stack and  nums[i]<=nums[stack[-1]]:
        while(stack and nums[i]<=nums[stack[-1]]):
            stack.pop()

        if len(stack)>0:
            right[i] = stack[-1]-1
        else:
            right[i] = n-1

    else:
        right[i] = i
        
    stack.append(i)


maxi = 0

for i in range(n):
    maxi = max(maxi , nums[i] * (right[i] - left[i]  + 1 )  )

print(maxi)