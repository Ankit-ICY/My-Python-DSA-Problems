
# def solve(nums,n,prev,ind,dp):

#     if ind>=n or prev>=n:
#         return 0


#     if prev == -1 or nums[ind]>nums[prev]  :
#         x1 = 1 + solve(nums,n,ind,ind+1,dp)
#         x2 = solve(nums,n,prev,ind+1,dp)
#         x = max(x1,x2)
#     else:
#         x = solve(nums,n,prev,ind+1,dp)

#     return x

# nums = [1, 11, 2, 10, 4, 5, 2, 1]
# n = len(nums)
# prev = -1
# ind = 0
# dp ={}
# print(solve(nums,n,prev,ind,dp))


nums = [1, 2, 5, 3, 2]
n = len(nums)
dp = [1]*n
ans = 0
for i in range(1,n):
    for j in range(0,i):

        if (nums[j] <nums[i] )   and dp[i] < 1 + dp[j] :
            dp[i] = 1 + dp[j]
            ans = max(ans,dp[i])
        

print(ans)