n = 5
edges =  [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 2
distance = [[1e9]*n for i in range(n)]

for i in edges:
    distance[i[0]][i[1]] = i[2]
    distance[i[1]][i[0]] = i[2]

for i  in range(n):
    distance[i][i] =  0


for k in range(n):
    for  i in range(n):
        for j in range(n):
            if distance[i][k] == 1e9 or distance[k][j]==1e9:continue

            distance[i][j] = min(distance[i][j] , distance[i][k] + distance[k][j] )

 
city  = -1
cityCount = n+1
for i in range(n):
    count = 0
    for j in range(n):
        if distance[i][j] <= distanceThreshold:
            count+=1

    if count<=cityCount:
        cityCount = count
        city = i

print(distance)
print(city)