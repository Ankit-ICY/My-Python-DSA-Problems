def solve(grid,i,j1,j2,r,c,dp):
    if j1 <0 or j1 >=c or j2 <0 or j2 >=c :
        return -1e8


    if i==r-1:
        if j1==j2:
            return grid[i][j1]
        else:
            return grid[i][j1] + grid[i][j2]


    
    maxi = -1e8
    for d1 in range(-1, 2):
        for d2 in range(-1,2):

            if j1 == j2 :
                value = grid[i][j1] 

            else:
                value = grid[i][j1]  + grid[i][j2] 

            maxi = max(maxi , value+ solve(grid,i+1,j1+d1,j2+d2,r,c,dp) )
    
    return maxi

grid = [ [3,1,1]
        ,[2,5,1]
        ,[1,5,5]
        ,[2,1,1]]


r = 4
c= 3
i = 0
j1 = 0
dp = {}
j2 = c-1
print(solve(grid,i,j1,j2,r,c,dp))