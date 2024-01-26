def solve(nums,ind,k,n,dp):
    if ind==n:
        return 0
    
    if (ind) in dp:
        return dp[(ind)]

    ans = 1e9
    jump = 0
    for i in range(1 , k+1):
        if ind+i<n:
            jump = abs(nums[ind] - nums[ind+i] ) + solve(nums,ind+i,k,n,dp)
        ans = min(ans, jump )

    dp[(ind)] = ans
    return ans

nums = [10 ,20, 10]
ind = 0
n  = 3
k = 1
print(solve(nums,ind,k,n,{})) 