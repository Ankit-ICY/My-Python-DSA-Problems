def solve(nums,ind,n,sum,dp):

    if n==0  :
        if sum==0 and nums[0] == 0:
                return 2
                
        if sum==0 or nums[0]==sum:
            return 1
                
        return 0



    if nums[n]<=sum:
        x1 = solve(nums,ind,n-1,sum-nums[n-1],dp)
        x2 = solve(nums,ind,n-1,sum,dp)
        x  = x1 + x2

    else:
        x = solve(nums,ind,n-1,sum,dp)

    return x

nums = [1,4,4,5]
n= 4
sum = 5
ind = 0
dp = {}
print(solve(nums,ind,n-1,sum,dp))