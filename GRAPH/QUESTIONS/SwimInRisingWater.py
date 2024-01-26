grid = [[0,2],[1,3]]


from heapq import heapify, heappop, heappush
heap = [[grid[0][0] ,[0,0]]]

n = len(grid)

vis = [[False]*n for _ in range(n)]


dr = [0,-1,0,1]
dc = [1,0,-1,0]
maxi = 0
while heap:

    cell = heappop(heap)
    dist = cell[0]
    row = cell[1][0]
    col = cell[1][1]
    maxi = max(maxi, dist)
    vis[row][col] = True
    if row == n-1 and col==n-1:
        print(maxi)
        break
    for i in range(4):
        newR  = dr[i] + row
        newC = dc[i] + col

        if newR>=0 and newR <n and newC>=0 and newC<n and not vis[newR][newC]:
            heappush(heap, [grid[newR][newC] , [newR,newC]])



