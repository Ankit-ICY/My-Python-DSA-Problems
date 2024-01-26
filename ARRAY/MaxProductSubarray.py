nums = [2,3,-2,4]

maxi = nums[0]
mini = nums[0]
ans = nums[0]

for i in range(1,len(nums)):
    ele = nums[i]
    x1 = ele
    x2 = maxi*ele
    x3 = mini *ele
    maxi = max(x1,x2,x3)
    mini = min(x1,x2,x3)
    ans = max(ans,maxi)
print(ans)



