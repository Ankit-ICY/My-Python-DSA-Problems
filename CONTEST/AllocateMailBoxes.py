def solve(nums,k , ind, dp,next):
    if k==0:
        return 0
    if ind>=len(nums)-1:
        return 0
    
    ans = 1e9
   
    if nums[next] - nums[ind] > 1: 
        for i in range(nums[ind]+1 , nums[next]):

            diff = (i - nums[ind]) + (nums[ind+1] - i) 
            ans = min(ans, diff  +  solve(nums,k-1 , i, dp , i+1)  )

    else:
        solve(nums,k , ind, dp,next+1)
            

    return ans


nums = [2,3,5,12,18]
k = 2
ind = 0
next = 1
dp = {}
print(solve(nums,k , ind, dp, next))