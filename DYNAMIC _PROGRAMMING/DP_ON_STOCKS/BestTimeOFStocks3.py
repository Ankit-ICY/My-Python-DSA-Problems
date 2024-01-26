def solve(ind,nums,flag,count , n,dp):
    if count == 0:
        return 0

    if ind>=n:
        return 0
    
    if (ind,flag,count) in dp:
        return dp[(ind,flag,count)]


    if flag == 1:
        x1 = -nums[ind] + solve(ind+1,nums,0,count , n,dp)
        x2 = solve(ind+1,nums,flag,count , n,dp)
        dp[(ind,flag,count)] = max(x1,x2)


    else:
        x1 = nums[ind] + solve(ind+1,nums,1,count-1 , n,dp)
        x2 = solve(ind+1,nums,flag,count , n,dp)
        dp[(ind,flag,count)]= max(x1,x2)



    return dp[(ind,flag,count)]


nums = [10 ,22 ,5 ,75 ,65 ,80]
n = 6
flag = 1
count = 2
ind = 0
dp = {}

print(solve(ind,nums,flag,count , n,dp))