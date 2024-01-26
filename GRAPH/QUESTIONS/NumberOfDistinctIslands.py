def solve(i, j , visited , ROW, COL , s):
    visited[i][j] = True
    q = [[i,j]]
    dr = [0,-1,0,1]
    dc = [1,0,-1,0]
    a = []
    while q:
        cell = q.pop(0)
        row = cell[0]
        col= cell[1]
        visited[row][col] = True
        a.append(ROW-row )
        a.append(COL-col)
        for i in range(4):
            newR = row + dr[i]
            newC = col + dc[i]
            if newR>=0 and newC>=0 and newR<n and newC<m and grid[newR][newC] and not visited[newR][newC]:
                q.append([newR,newC])

    return a

grid = [[1 ,1, 0, 1, 1],
        [1 ,0 ,0 ,0 ,0],
        [0 ,0, 0, 0, 1],
        [1 ,1 ,0 ,1, 1]]


n = len(grid)
m = len(grid[0])
visited =  [[False]*m for i in range(n)]
s = set()
for i in range(n):
    for j in range(m):
        if grid[i][j] and  not visited[i][j] :
            a = solve(i, j , visited , i, j , s)
            s.update(a)
    
print(len(s))