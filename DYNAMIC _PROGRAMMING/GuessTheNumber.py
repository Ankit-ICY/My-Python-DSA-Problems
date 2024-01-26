def solve(n,i,j):
    if i >= j:
        return 0

    ans = 1e9
    for k in range(i, j+1):

        x1 = k + solve(n,k+1,j)
        x2 = k + solve(n,i,k-1)
        x = max(x1,x2)
        ans = min(x, ans)

    return ans

n = 10
i = 1
j = n
dp = {}
print(solve(n,i,j))
