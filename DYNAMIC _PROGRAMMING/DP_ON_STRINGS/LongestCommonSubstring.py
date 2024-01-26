# def solve(s1,s2,n,m):
#     if m<0 or n<0:
#         return 0

#     ans = 0
#     if s1[n] == s2[m]:
#         x = 1 +  solve(s1,s2,n-1,m-1)
#         ans = max(ans,x)

#     else:
        
#         x = 0 +  solve(s1,s2,n-1,m) or  solve(s1,s2,n,m-1)

        

#     return ans
    

# s1 = "ABCDGH"
# s2 = "ACDGHR"
# n = 6
# m = 6

# print(solve(s1,s2,n-1,m-1))



s1 = "ABC"
s2 = "ACB"
n = 3
m = 3

dp = [[0]*(m+1) for _ in range(n+1)]

ans = 0
for i in range(1, n+1):
    for j in range(1,m+1):

        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
            ans = max(ans,dp[i][j])

        else:
            dp[i][j] = 0


print(ans)