def combSum(nums,ind,ans,total,n, target):

    if ind==n:
        if target==0:
            total.append(ans.copy())
        return ans  
        

    if nums[ind]<=target:
        ans.append(nums[ind])
        combSum(nums,ind,ans,total,n, target-nums[ind])
        ans.pop()
        combSum(nums,ind+1,ans,total,n, target)
    else:
        combSum(nums,ind+1,ans,total,n, target)


    return total


nums = [7,2,6,5]
target = 16
n = 4
ind= 0
ans =[]
total = []
print(combSum(nums,ind,ans,total,n ,target))