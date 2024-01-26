nums =[3,1,5,6,4,2]
n = len(nums)
left = [0]*n
right = [0]*n
pre = [0]*(n+1)
sum = 0
for i in range(1,n+1):
    sum +=nums[i-1]
    pre[i] = sum

stack = []
for i in range(n):
    while stack and nums[stack[-1]]>= nums[i]:
        stack.pop()


    if not stack:
        left[i] = -1

    else:
        left[i]= stack[-1]

    stack.append(i)


stack.clear()

for i in range(n-1, -1, -1):
    while stack and nums[stack[-1]] >= nums[i]:
        stack.pop()

    if stack:
        right[i] = stack[-1]
    else:
        right[i] = n

    stack.append(i)



maxi = 0
for i in range(n):
    diff = pre[right[i]] - pre[left[i]+1]
    maxi = max(maxi , diff* nums[i]  )

print(maxi)







