nums = [1,2,3,4,3]
n = len(nums)
# ans = [0]*len(nums)
stack = []
for i in range(2*n-1 , -1, -1):
    x = nums[i%n]
    while  stack and stack[-1]<=nums[i%n]:
        stack.pop()

    if i<n:
        if len(stack)>0:
            nums[i%n] = stack[-1]
        else:
            nums[i%n] = -1

    stack.append(x)


print(nums)