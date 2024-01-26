grid = [ [2,1,1]
        ,[1,1,1]
        ,[0,1,2]]



n = len(grid)
m = len(grid[0])
q = []
map =[]
for i in range(n):
    a = []
    for j in range(m):
        a.append(False)

    map.append(a)
count = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            q.append([i,j,0])
            map[i][j] = 2

        else:
            map[i][j] = 0

        if grid[i][j] == 1:
            count+=1

maxT = 0
drow = [-1,0,1,0]
dcol = [0,1,0,-1]
countF = 0
while len(q)!=0 :
    r = q[0][0]
    c =q[0][1]
    t = q[0][2]
    maxT = max(maxT,t)
    q.pop(0)
    for i in range(4):
        row = r + drow[i]
        col = c + dcol[i]
        if row>=0    and row<n and col>=0 and col<m and map[row][col]==0 and grid[row][col]==1:
            q.append([row,col,t+1])
            map[row][col] = 2
            countF+=1


if countF!= count:
    print(-1)
else:
    print(maxT)