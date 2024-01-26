def FindParent(node):
    if parent[node] == node:
        return node

    else:
        parent[node] = FindParent(parent[node])
        return parent[node]


def disjoint(u,v):

    ul_u = FindParent(u)
    ul_v = FindParent(v)
    if ul_u == ul_v:
        return

    if size[ul_v]>=size[ul_u]:
        parent[ul_u] = ul_v
        size[ul_v] += size[ul_u]
    else:
    
        parent[ul_v] = ul_u
        size[ul_u] += size[ul_v]


def isValid(row,col,m):
    return row>=0 and col>=0 and row<m and col<m

grid =  [ [0,0,0,0,0,0,0]
         ,[0,1,1,1,1,0,0]
         ,[0,1,0,0,1,0,0]
         ,[1,0,1,0,1,0,0]
         ,[0,1,0,0,1,0,0]
         ,[0,1,0,0,1,0,0]
         ,[0,1,1,1,1,0,0]]


m = len(grid)
n = m * m

parent = [0]*n
for i in range(n):
    parent[i] = i

size = [1] *n
dr = [0,-1,0,1]
dc = [1,0,-1,0]
for i in range(m):
    for j in range(m):
        if grid[i][j] == 1 :
            row = i
            col = j
            for k in range(4):
                newR = dr[k] + row
                newC = dc[k] + col

                if isValid(newR,newC, m) and grid[newR][newC]:
                        nodeNo = (row * m )+ col
                        adjNode = (newR * m) + newC
                        disjoint(nodeNo , adjNode)

                    
maxi = 0
count = 0
for i in range(m):
    for j in range(m):
        if grid[i][j] == 0:
            row= i
            col = j
            s = set()
            for k in range(4):
                newR = row  + dr[k]
                newC = col + dc[k]

                if isValid(newR, newC,m) and grid[newR][newC] == 1:
                    adjNode = (newR * m) + newC
                    ulp = FindParent(adjNode)
                    s.add(ulp)
        count = 0
        for x in s:
            count+= size[x]

        maxi = max(count+1,maxi)


print(maxi)


