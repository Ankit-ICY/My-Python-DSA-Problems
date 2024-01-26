
mat = [[0,0,0],[0,1,0],[1,1,1]]

m = len(mat)
n = len(mat[0])
visited = [[False]*n for i in range(m)]
q = []

for i in range(m):
    for j in range(n):
        if mat[i][j]==0:
            visited[i][j] = True
            q.append([0, [i, j]])


distance = [[1e9]*n for i in range(m)]

dr = [0,-1,0,1]
dc = [1,0,-1,0]

while q:
    cell = q.pop(0)
    step = cell[0]
    row = cell[1][0]
    col = cell[1][1]
    mat[row][col] = step
    for i in range(4):
        newR = row + dr[i]
        newC = col + dc[i]

        if newR>=0 and newC >=0 and newC<n and newR <m and not visited[newR][newC]:
            visited[newR][newC] = True
            # if  mat[newR][newC] == 1 and step + 1 < distance[newR][newC]:
            distance[newR][newC] = step + 1
            q.append([step+1, [newR, newC] ] )

         


print(mat)