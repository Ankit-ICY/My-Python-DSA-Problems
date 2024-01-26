nums = [13]

pre = nums[0]
ans = [0]*len(nums)
ans[0] = pre
for i in range(1,len(nums)):
    temp = pre
    pre = pre^nums[i]
    ans[i] = pre
    pre = pre ^ temp


print(ans)