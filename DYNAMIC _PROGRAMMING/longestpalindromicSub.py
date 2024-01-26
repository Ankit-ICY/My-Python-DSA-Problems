s = "babad"
n = len(s)
c = 0
dp = [[0] * n  for _ in range(n)]

maxi = -1
ans =""
for x in range(n):
    i = 0
    j = i+x
    while j<n :
        if i==j:
            dp[i][j] = 1

        elif x==1:
            if s[i] == s[j]:
                dp[i][j] = 2
            else:
                dp[i][j] = 0

        else:
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j] = dp[i+1][j-1] +2


        if dp[i][j]:
            if j-i+1>maxi:
                maxi = j-i+1
                ans = s[i:j+1]

        i+=1
        j+=1

    
print(ans)


