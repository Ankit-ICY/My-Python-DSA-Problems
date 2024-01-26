def CombSum(nums,ind,k,n,ans,res):
    if n==0 and len(ans)==k:
        res.append(ans.copy())
        return

    for i in range(ind,len(nums)):
        if nums[i]<=n:
            ans.append(nums[i])
            CombSum(nums,i+1,k,n-nums[i],ans,res)
            ans.pop()

    return res

k = 3
n = 7
nums= []

i=1
while(len(nums)!=n):
    nums.append(i)
    i+=1
    if i==10:
        i=1

ind = 0
print(CombSum(nums,ind,k,n,[],[]))