grid =  [[2,1,1],[1,1,0],[0,1,1]]
m = len(grid)
n = len(grid[0])
q = []
count = 0
visited = [[False]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        if grid[i][j] == 2:
            q.append([0,[i,j]])

        elif grid[i][j] == 1:
            count+=1

dr = [1,0,-1,0]
dc  = [0,-1,0,1]
ans = 0
countF = 0
while q:
    cell = q.pop(0)
    time = cell[0]
    row = cell[1][0]
    col = cell[1][1]
    ans = max(ans, time)
    for i in range(4):
        newR = row + dr[i]
        newC= col + dc[i]
        if newR>=0 and newC >=0 and newR<m and newC <n and grid[newR][newC] ==1 and not visited[newR][newC]:
            visited[newR][newC] = True
            q.append([time+1, [newR,newC]])
            countF+=1


if countF != count:
    print(-1)