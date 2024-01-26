def isValid(nums1, nums2):
    for i in range(3):
        if nums1[i]>nums2[i]:
            return False
        
    
    return True


def solve(nums,dp,ind, prev):
    if ind>=len(nums):
        return 0

    x = 0
    if prev == -1 or isValid(nums[prev] , nums[ind]):
        x1 = nums[ind][-1] +  solve(nums,dp,ind+1, ind)
        x2 = solve(nums,dp,ind+1, prev)

        x = max(x1,x2)

    else:
        x = solve(nums,dp,ind+1, prev)

    return x
    

nums =[[50,26,84],[2,55,62],[64,63,72]]



for i in range(len(nums)):
    nums[i].sort()

nums.sort()
dp ={ }
ind = 0
print(solve(nums,dp,ind, -1))
