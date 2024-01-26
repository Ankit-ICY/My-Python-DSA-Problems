def findSafeDist(row,col,cells):
    temp = []
    for it in cells:
        dist1 = abs(it[0] - row )
        dist2 = abs(it[1]-col)

        temp.append(  dist1+dist2 )

    return min(temp)

grid = [ [0,1,1]
        ,[0,0,0]
        ,[0,0,0]]



cells =[]
vis=  []
n = len(grid)
for i in range(n):
    a = []
    for j in range(n):
        if grid[i][j]:
            cells.append([i,j])

        a.append(False)
    
    vis.append(a)

d = findSafeDist(0,0,cells)


heap = [[-d,0,0]]
dr = [1,0,-1,0]
dc = [0,-1,0,1]
ans = 1e9
from heapq import heapify, heappop, heappush
while heap:
    cell = heappop(heap)
    row = cell[1]
    col  = cell[2]
    distance = cell[0]
    vis[row][col] =True
    temp = abs(distance)
    ans = min(temp,ans)
    if row == n-1 and col == n-1:
        print(ans)
        break
    for i  in range(4):
        newR = row + dr[i]
        newC = col + dc[i]

        if newR<n and newC <n and newR>=0 and newC>=0  and not grid[newR][newC] and  not vis[newR][newC] :
            d = findSafeDist(newR,newC , cells)

            heappush(heap , [-d , newR, newC ])

            


