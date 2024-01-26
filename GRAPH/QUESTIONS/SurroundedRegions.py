def solve(i,j, visited):
    visited[i][j] = True
    q = [[i,j]]
    dr = [0,1,0,-1]
    dc = [-1,0,1,0]
    while q:
        cell = q.pop(0)
        row = cell[0]
        col = cell[1]
        for i in range(4):
            newR = row + dr[i]
            newC = col + dc[i]
            if newR>=0 and newC>=0 and newR<m and newC<n and board[newR][newC] == "O" and not visited[newR][newC]:
                visited[newR][newC] = True
                q.append([newR, newC])


board = [["X","O","X","O","X","O"]
         ,["O","X","O","X","O","X"]
         ,["X","O","X","O","X","O"]
         ,["O","X","O","X","O","X"]]

m =len(board)
n = len(board[0])

visited = [[False]*n for i in range(m)]

for i in range(m):
    for  j in range(n):
        if board[i][j] == "O" and not visited[i][j]:
            if i==0 or i==m-1 or j==0 or j==n-1:
                solve(i,j, visited)


for  i in range(m):
    for j in range(n):
        if board[i][j]=="O" and not visited[i][j] :
            board[i][j]="X"


print(visited)
print(board)