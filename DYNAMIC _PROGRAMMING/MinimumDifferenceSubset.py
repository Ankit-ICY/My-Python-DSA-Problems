# nums = [1,6,11,5]
# n = len(nums)
# dp = []
# total = sum(nums)
# for i in range(n):
#     a = []
#     for j in range(total+1):
#         a.append(False)
#     dp.append(a)


# for i in range(n):
#     dp[i][0] = True


# for i in range(1,n):
#     for j in range(1,total+1):
#         if nums[i-1] > j:
#             dp[i][j] = dp[i-1][j] # NOT TAKE 

#         else:
#             dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

# ans = 1e9
# for i in range((total//2)+1):
#     if dp[n-1][i]:
#         ans = min(ans,(total -i)-i)

# print(ans)






def Solve(ind,nums,total,ans,add,dp,n):

    if ind == n:
        if add<total and add not in ans:
            ans.append(add)
        return 0
    if (ind,add) in dp:
        return dp[(ind,add)]
    
    for i in range(ind,n):
      
        x = Solve(i+1,nums,total,ans,add+nums[i],dp,n)
        dp[(ind,add)] = x
    return ans


nums = [1,6,11,5]
total = sum(nums)
n = len(nums)
if n==1:print(nums[0])
else:
    sol = Solve(0,nums,total,[],0,{} , n)

    final = 1e9
    for i in sol:
        left = total-i
        final = min(final , abs(left-i))

    print(final)






