def CombSum(nums,target,ind,ans,res ,dp):

    if target==0  and ans not in res:
        res.append(ans.copy())
        return 
    

    for i in range(ind,len(nums)):
        # if i>ind and nums[i]==nums[i-1]:continue
        # if nums[i]>target:break
        if nums[i]<=target:
            ans.append(nums[i])
            CombSum(nums,target-nums[i],i+1,ans,res, dp)
            ans.pop()


    return res


nums = [10,1,2,7,6,1,5]
target= 8
nums.sort()
ind = 0
ans =[]
res = []
print(CombSum(nums,target,ind,ans,res,{}))