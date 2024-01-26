def solve(nums,ind,dp,prev):
    if ind == len(nums)-1:
        return 0
    
    if ind>=len(nums):
        return 0
    
    if (ind,prev) in dp:
        return dp[(ind,prev)]


    x1 = abs(nums[ind]- nums[ind+1]) +  solve(nums,ind+1,dp,ind)
    x2 = 1e9
    if ind+2<len(nums):  
        x2 =  abs(nums[ind]- nums[ind+2]) + solve(nums,ind+2,dp,ind)
    dp[(ind,prev)]= min(x1,x2)

    return dp[(ind,prev)]


nums = [10,20,30,10]
ind = 0
dp ={}
prev = 0
print(solve(nums,ind,dp,prev))