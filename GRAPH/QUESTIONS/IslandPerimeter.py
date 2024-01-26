grid = [[1,1],[1,1]]


row =len(grid)
col = len(grid[0])
flag = 0
vis = [[False]*col for _ in range(row)]
q = []
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1:
            q = [[i,j,4]]
            vis[i][j] = True
            flag = 1
            break

    if flag==1:
        break


ans = 0
dr = [0,1,0,-1]
dc = [-1,0,1,0]
while q:
    cell = q.pop(0)
    r = cell[0]
    c = cell[1]
    peri = cell[2]
    for i in range(4):
        newR = r + dr[i]
        newC = c + dc[i]

        if newR>=0 and newC>=0 and newR<row and newC<col and not vis[newR][newC] and grid[newR][newC]:
            peri = peri-1
            vis[newR][newC] = True
            q.append([newR,newC,4])

        elif newR>=0 and newC>=0 and newR<row and newC<col and vis[newR][newC]:
            peri-=1

    ans+=peri


print(ans)