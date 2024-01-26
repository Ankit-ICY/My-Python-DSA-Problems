grid =[[0]]




n = len(grid)
distance = [[1e9]*n for  i in range(n)]
q = []
q.append([1 , [0,0]])

dr  = [0,1,0,-1 , 1 ,-1, 1, -1]
dc = [-1,0,1,0  ,-1 , 1, 1, -1]
while(q):
    node = q.pop(0)
    dist = node[0]
    row = node[1][0]
    col = node[1][1]
    if row == n-1 and col == n-1:
        print(distance[row][col])
        break

    for  i in range(8):
        newrow= row + dr[i]
        newcol = col + dc[i]
        if newrow>=0 and newcol>=0 and newrow<n and newcol<n and grid[newrow][newcol]!= 1:
            newDist = dist + 1
            if newDist<distance[newrow][newcol]:
                distance[newrow][newcol] = newDist
                q.append([newDist ,[newrow,newcol]])






