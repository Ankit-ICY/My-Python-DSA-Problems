def jumpGame(nums,k,ind,dp,n):
    if ind>=n:
        return 0
    if ind==n-1:
        return nums[n-1]
    
    ans = -1e9
    for i in range(ind+1, min(n , ind+k+1)):
        ans = max(ans, nums[ind] + jumpGame(nums,k,i,dp,n))
    return ans

nums =  [1,-1,-2,4,-7,3]
k = 2
ind = 0
dp = {}
n = len(nums)
print(jumpGame(nums,k,ind,dp,n))