def solve(nums,dp,n,ind):
    
    if n==0:
        return 0

    if ind>=len(nums):
        return -1e9
    
    if (n,ind) in dp:
        return dp[(n,ind)]

    x = 0
    if nums[ind]<=n:
        x1 = 1 + solve(nums,dp,n-nums[ind],ind)
        x2 = solve(nums,dp,n,ind+1)
        x = max(x1,x2)
        dp[(n,ind)]= x
    else:
        x = solve(nums,dp,n,ind+1)    
        dp[(n,ind)] = x

 
    return x
nums = [ 1 ,4 ,4]
n = 8

dp= {}

print(solve(nums,dp,n,0))
