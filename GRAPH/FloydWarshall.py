edges = [[1 ,2 ,2],[1, 3 ,2],[2 ,3 ,-1 ]]
n = 3
m = 3
src = 1
dst = 3


distance = [[1e9]*(n+1) for i in range(n+1)]


for i in range(m):
    distance[edges[i][0]][edges[i][1]] = edges[i][2]


for i in range(1,n+1):
    distance[i][i] = 0


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][k] == 1e9 or distance[k][j] ==1e9 :continue

            distance[i][j] = min(distance[i][j] , distance[i][k] + distance[k][j] )


print(distance[src][dst])





