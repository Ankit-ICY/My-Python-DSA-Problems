nums = [73,74,75,71,69,72,76,73]


n = len(nums)
temp = [0]*n

stack = []
for i in range(n-1, -1, -1):
    count = 0
    total = 0
    while stack  and nums[stack[-1]]  <= nums[i]:
        num = stack.pop()


    if stack:
        temp[i] = stack[-1] - i

    stack.append(i)

print(temp)