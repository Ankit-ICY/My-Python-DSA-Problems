def subsetSum(nums,n,ind,ans, res):
    
    res.append(sum(ans))

    for i in range(ind,n):
        ans.append(nums[i])
        subsetSum(nums,n,i+1,ans, res)
        ans.pop()

    return res

nums = [5, 2, 1]
n = 3
ind = 0
ans = []
res = []
subsetSum(nums,n,ind,ans, res)
res.sort()
print(res)