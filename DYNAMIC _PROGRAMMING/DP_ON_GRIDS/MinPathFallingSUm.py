def solve(i,j,matrix,dp,n):

    if j>=n or i>=n :
        return 0

    if i == n-1:
        return matrix[i][j]
    

    x1 = matrix[i][j] +   solve(i+1,j,matrix,dp,n)
    x2 = matrix[i][j] +  solve(i+1,j+1,matrix,dp,n)
    x3 = matrix[i][j] +  solve(i+1,j-1,matrix,dp,n)

    x = max(x1,x2,x3)

    return x
    


matrix =[[348, 391],[618, 193]]
n = len(matrix)
j = 0
dp = {}
ans = 0
for j in range(n):
    ans = max(ans , solve(0,j,matrix,dp,n))


print(ans)