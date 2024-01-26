edges = [[2,1] , [2,0]]
n  = 3
m = 2
graph = {}
for i in range(m):
    if edges[i][0] not in graph:
        graph[edges[i][0]] = [edges[i][1]]

    else:
        graph[edges[i][0]].append(edges[i][1])

    
    if edges[i][1] not in graph:
        graph[edges[i][1]] = [edges[i][0]]

    else:
        graph[edges[i][1]].append(edges[i][0])

print(graph)