image = [[0,0,0],[0,0,0]]

sr = 1
sc = 0
color = 2
m = len(image)
n = len(image[0])
q = [[image[sr][sc],[sr,sc]] ]
image[sr][sc] = color

dr = [0,1,0,-1]
dc = [-1,0,1,0]

while q:
    cord = q.pop(0)
    c = cord[0]
    row = cord[1][0]
    col = cord[1][1]

    for i in range(4):
        newR = row + dr[i]
        newC = col + dc[i]

        if newR>=0 and newC>=0 and newC<n and newR<m  and image[newR][newC] == c :  
            image[newR][newC] = color
            q.append([c, [newR,newC]] )


print(image)