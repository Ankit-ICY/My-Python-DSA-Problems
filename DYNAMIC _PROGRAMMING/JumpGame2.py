def JumpGame(nums,ind,dp):
    if ind>=len(nums)-1:
        return 0
    
    x = 1e9
    for i in range(1, nums[ind]+1):
        x = min(x,1 + JumpGame(nums,ind+i,dp))

    return x

nums = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]


ind = 0
dp ={}
print(JumpGame(nums,ind,dp))