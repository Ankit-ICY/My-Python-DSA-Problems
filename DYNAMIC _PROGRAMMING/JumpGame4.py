def solve(ind, dp , nums,visited ):
        
    if ind<0 or ind>=len(nums) or visited[ind]==True:
        return 1e9
    
    if ind==len(nums)-1:
        return 0



    visited[ind] = True
    x1  =  1 +  solve(ind+1, dp , nums ,visited)
    x2 = 1 + solve(ind-1, dp , nums,visited )
    x3 = 1e9
    for i in range(ind, len(nums)):
        if nums[ind] == nums[i]:
            x3 = min(x3, 1 + solve(i, dp , nums ,visited ))
    visited[ind] = False

    x = min(x1,min(x2,x3))

    return x

nums = [100,-23,-23,404,100,23,23,23,3,404]
dp = {}
visited = [False]*len(nums)
ind = 0
print(solve(ind, dp , nums ,visited))


