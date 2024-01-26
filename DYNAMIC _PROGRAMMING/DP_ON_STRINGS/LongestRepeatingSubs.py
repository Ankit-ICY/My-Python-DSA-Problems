# def solve(s1,s2,i,j,dp):

#     if i>=len(s1) or j>=len(s2):
#         return 0


#     if s1[i]==s2[j] and i!=j:
#         x = 1 + solve(s1,s2,i+1,j+1,dp)

#     else:
#         x1 = solve(s1,s2,i+1,j,dp)
#         x2 = solve(s1,s2,i,j+1,dp)
#         x = max(x1,x2)

#     return x

# s1 = "axxzxy"
# s2 = s1
# i =0 
# j = 0
# dp ={}
# print(solve(s1,s2,i,j,dp))

s1 = "axxzxy"
s2= s1
m = len(s1)
n = len(s2)
dp = [[0]*(n+1) for i in range(m+1)]
ans = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i-1] == s2[j-1] and i!=j:
            dp[i][j] = 1 + dp[i-1][j-1]
            ans = max(ans,dp[i][j])

        else:
            dp[i][j] = max(dp[i-1][j] , dp[i][j-1])


print(ans)
