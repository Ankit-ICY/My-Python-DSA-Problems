n=7
start = [1, 1]
target= [7, 5]


dr = [-2, -2, 1, -1, -1,  1, 2,  2]
dc = [1,-  1, 2,  2, -2, -2, -1, 1]
start.append(0)
vis = [[False]*n for _ in range(n)]
q = [start]
ans = 1e9
while q:
    cell = q.pop(0)
    row = cell[0]
    col = cell[1]
    # vis[row][col] = True
    step = cell[2]
    if row == target[0] and col == target[1] :
        ans = min(ans,step)
    for i in range(8):
        newR = dr[i] + row
        newC = dc[i] + col
        if newR>=0 and newC>=0 and newR<n and newC<n and not vis[newR][newC]:
            vis[newR][newC] = True
            q.append([newR,newC,step+1])



print(ans)