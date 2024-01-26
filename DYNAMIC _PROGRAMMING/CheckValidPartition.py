def solve(nums,ind,dp,n):
    if ind>=len(nums):
        return True

    x = False

    if ind+1<n and nums[ind] == nums[ind+1]:
        x |=  solve(nums,ind+2,dp,n)
   
    if ind+2 <n and nums[ind] == nums[ind+1] and nums[ind] ==nums[ind+2]:
        x |= solve(nums,ind+3,dp,n)
   
        
    if ind+2<n and (nums[ind+1] - nums[ind]) == 1 and (nums[ind+2]  -nums[ind+1]) == 1:
        x |= solve(nums,ind+3,dp,n)
 
 
    return x


nums = [803201,803201,803201,803201,803202,803203]
ind = 0
dp = {}
n = len(nums)
print(solve(nums,ind,dp,n))