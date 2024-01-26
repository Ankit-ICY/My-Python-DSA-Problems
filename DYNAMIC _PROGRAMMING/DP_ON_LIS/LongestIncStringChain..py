def helper(s1,s2):
    if len(s1)!=len(s2)+1:return False

    c=0
    x ,y = 0,0
    while(x<len(s1) and y<len(s2)):
        if s1[x]==s2[y]:
            x+=1
            y+=1
            c+=1
        else:
            x+=1
    if c==len(s1)-1:
        return True
    else:return False

words = ["a","b","ba","bca","bda","bdca"]

n= len(words)
dp = [1]*n
words = sorted(words , key=len)
ans = 1
for i in range(1,n):
    for j in range(0,i):
        if helper(words[i], words[j] ) and dp[i] < 1 + dp[j]:
            dp[i] = 1 + dp[j]
            ans = max(ans,dp[i])

    
print(ans)