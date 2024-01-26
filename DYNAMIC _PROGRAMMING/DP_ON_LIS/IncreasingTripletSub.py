nums  = [1,2,3,4,5]
n = len(nums)
dp = [1] *n

for i in range(n-2, -1,-1):
    for j in range(n-1,i,-1):

        if nums[j]>nums[i] and dp[i] <dp[j]+1:
            dp[i] = 1 + dp[j]
            
print(dp)