class Solution:
    def minimumCostPath(self, grid):
        dp = {}
        i  = 0
        j = 0
        return self.solve(dp,i,j,grid)
    
    
    def solve(self,dp,i,j,grid):
        if i==len(grid)-1 and j==len(grid[0])-1:
            return grid[i][j]
            
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return 1e9
            
            
        down = grid[i][j] + self.solve(dp,i+1,j,grid)
        left = grid[i][j] + self.solve(dp,i,j-1,grid)
        right= grid[i][j] + self.solve(dp,i,j+1,grid)
        up =   grid[i][j] + self.solve(dp,i-1,j,grid)
        x = min(down,right,left,up)
        
        
        return x


grid =  [[9,4,9,9]
        ,[6,7,6,4],
         [8,3,3,7]
,        [7,4,9,10]]
ob = Solution()

ob.minimumCostPath(grid)
