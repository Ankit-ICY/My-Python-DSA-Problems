heights = [ [1,2,2,3,5],
            [3,2,3,4,4],
            [2,4,5,3,1]
           ,[6,7,1,4,5]
           ,[5,1,1,2,4]]


pac = set()
atl = set()
row = len(heights)
col = len(heights[0])
vis = [[0]*col for _ in range(row)]

q = []
for i in range(col):

    pac.add((0,i))
    q.append([0,i])
    vis[0][i] = 1


for i in range(row):
    pac.add((i,0))
    q.append([i,0])
    vis[i][0] = 1

dr = [1,0]
dc = [0,1]


while q:
    cell =q.pop(0)
    r = cell[0]
    c = cell[1]


    for i in range(2):
        newR = r + dr[i]
        newC = c + dc[i]

        if newR<row and newC<col and not vis[newR][newC]  and heights[r][c] <= heights[newR][newC]:
            vis[newR][newC] = 1
            q.append([newR,newC])
            pac.add((newR,newC))



for i in range(row):
    q.append([row-1,i])
    # vis[row-1][i] = 1
    

for j in range(col):
    q.append([j,col-1 ])
    # vis[j][col-1] = 1



dr = [-1,0]
dc = [0,-1]

ans = []

while q:
    cell = q.pop(0)
    r = cell[0]
    c = cell[1]

    for i in range(2):
        newR = r + dr[i]
        newC = c + dc[i]
        if newR>=0 and newC>=0 and  vis[newR][newC]  and heights[r][c] <= heights[newR][newC]:
   
            ans.append([newR,newC])
            q.append([newR,newC])


print(ans)

