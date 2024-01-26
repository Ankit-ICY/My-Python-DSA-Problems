def cost(left,right,s):
    count = 0
    while(left < right ):
        if s[left]!=s[right]:
            count+=1

        left +=1
        right-=1

    return count

def solve(s,ind,dp,k):
    if ind>=len(s):
        return 0
    
    if k==0:
        return 1e9


    x = 1e9

    for i in range(ind,len(s)):        
        x = min(x,cost(ind,i,s) + solve(s,i+1,dp,k-1))

    return x

s = "tcymekt"
k = 4
ind  = 0
dp = {}
print(solve(s,ind,dp,k))