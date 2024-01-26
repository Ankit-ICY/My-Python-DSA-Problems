import math
def solve(n,ind,dp,a):
    if n == 0:
        return 0
    x = 1e9

    if (n,ind) in dp:
        return dp[(n,ind)]
    for i in range(ind,a):
        sq = i **2

        if sq<=n:
            x = min(x, 1 + solve(n-sq,i,dp,a))
            dp[(n,ind)] = x

        else:
            break

    dp[(n,ind)] = x
    return x


    


n =  7334

ind = 1
a= math.isqrt(n)+1

dp ={}
print(solve(n,ind,dp,a))

