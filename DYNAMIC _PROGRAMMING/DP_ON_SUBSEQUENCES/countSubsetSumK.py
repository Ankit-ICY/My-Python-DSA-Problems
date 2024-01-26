def solve(ind,nums,k,dp):
    if k==0:
        return 1
    

    if ind==len(nums):
        return 0

 

    x = 0
    for  i in range(ind,len(nums)):
        if nums[i]<=k:
            x += solve(i+1,nums,k-nums[i],dp)
        

    return x



nums = [1,1,4,5]
k = 5
ind = 0
dp = {}
print(solve(ind,nums,k,dp))