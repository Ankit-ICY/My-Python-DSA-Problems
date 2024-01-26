def solve(i , j ,visited ):

    visited[i][j] = True
    
    q = [[i,j]]
    dr = [0,1,0,-1]
    dc = [-1,0,1,0]
    while(q):

        cell = q.pop(0)
        row = cell[0]
        col = cell[1]
        for i in range(4):
            newR = row + dr[i]
            newC = col + dc[i]
            if newR>=0 and newC>=0 and newR<m and newC<n and grid[newR][newC] == 1 and not visited[newR][newC]:
                visited[newR][newC] = True
                q.append([newR, newC])



grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]

m = len(grid)
n = len(grid[0])
visited = [[False]*n for i in range(m)]
ans = 0

for i in range(m):
    for j in range(n):
        if grid[i][j]==1 and  not visited[i][j] :
            if i==0 or i==m-1 or j==0 or j==n-1:
                solve(i,j, visited)


count =0
for  i in range(m):
    for j in range(n):
        if grid[i][j] == 1 and visited[i][j] == False:
            count+=1


print(count)