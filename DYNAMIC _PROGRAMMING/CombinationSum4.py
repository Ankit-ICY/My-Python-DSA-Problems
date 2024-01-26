def solve(nums,target, dp , ind):
    if target == 0:
        return 1

    x = 0
    for i in range(len(nums)):
        if nums[i]<=target:
            x = x+ solve(nums,target-nums[i], dp , i)

            
    return x

nums = [9]
target = 3

dp ={}
ind = 0
print(solve(nums,target, dp , ind))