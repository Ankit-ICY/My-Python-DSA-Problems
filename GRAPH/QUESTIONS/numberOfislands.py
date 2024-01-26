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

    if size[ul_v]>size[ul_u]:
        parent[ul_u] = ul_v
        size[ul_v] += size[ul_u]
    else:
    
        parent[ul_v] = ul_u
        size[ul_u] += size[ul_v]


  
    
islands = [ [0,0]
           ,[1,1]
           ,[2,2]
           ,[3,3]]

rows = 4
cols = 5
k = 4

n = (rows * cols)
size = [1]*n
parent = [0]*n

vis = [[False]*cols for _ in range(rows) ]

dr = [0,-1,0,1]
dc = [1,0,-1,0]
ans =[ ]
count = 0
for i in islands:
    row = i[0]
    col = i[1]


    if  vis[row][col]:
        ans.append(count)
        continue


    vis[row][col] = True
    count+=1
    for k in range(4):
        newR = row + dr[k]
        newC = col + dc[k]
        if newR>=0 and newC>=0 and newR < rows and newC< cols:
            if vis[newR][newC]:
                count-=1
                nodeNo = row * cols + col
                adjNode = newR * cols + newC

                disjoint(nodeNo, adjNode)
        
    ans.append(count)



print(ans)




