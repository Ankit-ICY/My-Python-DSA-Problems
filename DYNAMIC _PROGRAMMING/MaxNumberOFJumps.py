def solve(nums,target,prev,ind,dp,n):
    
    if ind>=n:
        return float('-inf')

    if ind==n-1:
        return 0

    maxi = float('-inf')
    for i in range(ind+1,n):
        if (nums[i] - nums[ind] <=target and nums[i]-nums[ind]>= -target):
            maxi = max( maxi , 1 + solve(nums,target,prev,i,dp,n))

    return maxi 


nums = [0,1,3,2,4]

target = 1
prev = 0
ind = 0
dp = {}
n = len(nums)
print(solve(nums,target,prev,ind,dp,n))

