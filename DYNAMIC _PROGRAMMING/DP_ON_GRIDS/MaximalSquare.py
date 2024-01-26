def solve(i,j,dp,matrix,m,n):
    if i>=m or j>=n:
        return 0
    
    if matrix[i][j] == "0":
        return 0 

    if (i,j) in dp:
        return dp[(i,j)]
    

    maxi = 0
    right =1 +  solve(i,j+1,dp,matrix,m,n)
    diagonal = 1 + solve(i+1,j+1,dp,matrix,m,n)
    down = 1 + solve(i+1,j,dp,matrix,m,n)

    dp[i,j] = min(right , diagonal , down)
    maxi = max(dp[i,j], maxi)


    return maxi

matrix =[["1","0"]
         ,["1","0"]]



i = 0
j = 0
dp ={}
m = len(matrix)
n = len(matrix[0])
ans = 0
maxi = [0]
for i in range(m):
    for j in range(n):
        if matrix[i][j] == "1" :
            ans = max(ans,solve(i,j,dp,matrix,m,n))


print(ans)