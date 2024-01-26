def solve(n,nums,ind,sum,dp):
    if sum==0:
        return 1

    if ind>=n:
        return 0
    
    

    if nums[ind] <= sum:
        x1 = solve(n,nums,ind+1,sum-nums[ind],dp)
        x2 = solve(n,nums,ind+1,sum,dp)
        x = x1 or x2
        return x

    else:
        x =  solve(n,nums,ind+1,sum,dp)
        return x

    return 0
    





n = 6
nums = [3, 34, 4, 12, 5, 2]
sum = 30
ind = 0
dp = {}
print(solve(n,nums,ind,sum,dp))