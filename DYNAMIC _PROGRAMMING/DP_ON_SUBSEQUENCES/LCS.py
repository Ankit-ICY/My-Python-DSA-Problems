
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

# print(dp)

i = m
j = n 
ans = ""
while i> 0 and j>0:
    if s1[i- 1] == s2[j-1]:
        ans += s1[i- 1]
        i-=1
        j-=1

    elif dp[i-1] > dp[j-1]:
        i-=1
        ans += s2[j-1]

    else:
        j-=1
        ans+=s1[i-1]


ans = ans[::-1]


# [   [0, 0, 0, 0, 0, 0, 0]
#  ,  [0, 1, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 1, 0, 0, 0, 0]
#   , [0, 0, 0, 2, 0, 0, 0]
#   , [0, 0, 0, 0, 3, 0, 0]
#   , [0, 0, 0, 0, 0, 4, 0]    ]

