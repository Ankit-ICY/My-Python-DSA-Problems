def solve(ind,dp,n,k):
    if n == 0:
        return 1
    
    if ind>n:
        return 0

    x = 0
    sol = ind**k
    if  ind**k <= n:
        x1 = solve(ind+1,dp,n-sol ,k)
        x2 = solve(ind+1,dp,n,k)
        x  =  x1 + x2

    return x


n = 4
k = 1

ind = 1
print(solve(ind,{},n,k))