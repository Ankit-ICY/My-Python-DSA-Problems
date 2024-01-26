# def ninjaTraining(grid,i,dp,n,last ):
#     if i==n:
#         return 0

#     ans = 0

#     for j in range(3):
#         if last == -1 or  j != last:
#             ans=  max(ans,grid[i][j] + ninjaTraining(grid,i+1,dp,n,j ))

    
#     return ans

    

# grid= [ [1,2,5]
#        ,[3,1,1],
#         [3,3,3]]



# i = 0
# dp = {}
# n = len(grid)
# last = -1
# print(ninjaTraining(grid,i,dp,n,last ))




grid= [ [1,2,5]
       ,[3,1,1],
        [3,3,3]]
n = len(grid)

dp = []
for i in range(n):
    a = [ ]
    for j in range(4):
        a.append(0)

    dp.append(a)



dp[0][0] = max(grid[0][1] , grid[0][2] )
dp[0][1] = max(grid[0][0] , grid[0][2] )
dp[0][2] = max(grid[0][1] , grid[0][0] )
dp[0][3] = max(grid[0][0] , grid[0][1], grid[0][2] )

for i in range(1,n):
    for j in range(0, 4):
        dp[i][j] = 0
        for k in range(3):
            if k!=j:
                point = grid[i][k] + dp[i-1][k]
                dp[i][j] = max(dp[i][j] , point)



    
print(dp[n-1][3] )


