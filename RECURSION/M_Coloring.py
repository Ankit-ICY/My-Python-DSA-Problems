def isPossible(m, edges,node, color,n):
    for i in range(len(edges)):
        if edges[i][0] == node or edges[i][0]==node:
            if color[edges[i][0]] == m and color[edges[i][1]] ==m:
                return False
            
    return True
    

def MCOLORING(n,m,edges,color,node):
    if n==node:
        return True

    for i in range(1, m+1):
        if isPossible(i, edges,node, color,n):
            color[node] = m
            return MCOLORING(n,m,edges,color,node+1)
            color[node] = 0

    return False


n = 4
m= 3
e = 5
edges = [[0,1],[1,2],[2,3],[3,0],[0,2]]
color =[0]*n

for i in range(n):
    color[i]=0

print(MCOLORING(n,m,edges,color,0))