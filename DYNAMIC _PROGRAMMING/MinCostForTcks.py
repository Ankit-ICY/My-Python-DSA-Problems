def solve(nums, costs, dp , ind):
    if ind>=len(nums):
        return 0



    # CASE 1 

    x1  = costs[0]+ solve(nums, costs, dp , ind+1)

    i = ind
    # CASE 2 
    while i<len(nums)  and nums[ind] + 7 > nums[i]:
        i+=1
    x2 = costs[1] + solve(nums, costs, dp ,i)
    

    i = ind
    while i<len(nums) and nums[ind] + 30 > nums[i]:
        i+=1

    x3 = costs[2] + solve(nums, costs, dp , i)

    x = min(x1,x2,x3)

    return x




nums = [1,2,3,4,5,6,7,8,9,10,30,31]
costs = [2,7,15]


dp ={}

ind = 0


print(solve(nums, costs, dp , ind))