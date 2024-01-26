# def solve(s1,s2,m,n):
#     if m<0 or n<0:
#         return 0 

#     if s1[m]!= s2[n]:
#         x1 =solve(s1,s2,m,n-1)
#         x2 = solve(s1,s2,m-1,n)

#         x = max(x1,x2)
#     else:
#         x = 1 + solve(s1,s2,m-1,n-1)

#     return x


# s1 = "ABC"
# s2 = "AC"
# m = 3
# n = 2

# print(solve(s1,s2,m-1,n-1))

s1 = "ABCDGH"
s2 = "ACDGHR"

m = 6
n = 6
dp = [[0]*(n+1) for i in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if s1[i- 1] == s2[j-1] :
            dp[i][j] = 1 +dp[i-1][j-1]

        else:
            dp[i][j] = 0

print(dp)
