# def solve(ind,nums,dp,n,total,sum):
#     dp.append(sum)


#     for i in range(ind,n):
#         sum+=nums[i]
#         solve(i+1,nums,dp,n,total,sum)
#         sum-=nums[i]


#     return dp


    
    

# nums = [3,9,7,3]
# ind = 0
# dp = []
# n = len(nums)
# total  = 72
# l =0

# print(solve(ind,nums,dp,n,total,l ))
# print(total)
# ans = 1e9
# for i in range(len(dp)):
#     sum  = abs(total-dp[i])
#     ans = min(ans ,  abs(sum-dp[i]) )

# print(ans)
nums = [3,9,7,3]
n = len(nums)
dp = []
total = sum(nums)
for i in range(n):
    a = []
    for j in range(total+1):
        a.append(False)
    dp.append(a)


for i in range(n):
    dp[i][0] = True


for i in range(1,n):
    for j in range(1,total+1):
        if nums[i-1] > j:
            dp[i][j] = dp[i-1][j] # NOT TAKE 

        else:
            dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

ans = 1e9
for i in range((total//2)+1):
    if dp[n-1][i]:
        ans = min(ans,(total -i)-i)