class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def solve(m,n,k,i,j):

            if i>=m or j>=n or i<0 or j<0:
                return 1

            if k==0:
                return 0

            left = solve(m,n,k-1,i,j-1)
            right = solve(m,n,k-1,i,j+1)
            up = solve(m,n,k-1,i-1,j)
            down = solve(m,n,k-1,i+1,j)

            ans = left + right + up + down

        
            return ans


        return solve(m,n,maxMove,startRow,startColumn)
    


ob = Solution()
m = 1
n = 3
maxMove = 3
startRow = 0
startColumn = 1

ans = ob.findPaths(m ,n, maxMove, startRow, startColumn)
print(ans)