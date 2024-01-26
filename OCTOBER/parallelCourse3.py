n = 3
relations = [[1,3],[2,3]]
time = [3,2,5]

maxi = {}

adj = [[] for _ in range(n+1)]
for i , j in relations:
    adj[i].append(j)



q = [1,2] 

while q:

    node = q.pop(0)
    
    if node not in maxi:
        maxi[node] = time[node-1]
        for nei in adj[node]:
            if nei not in maxi:
                maxi[nei ] = maxi[node]+ time[nei-1]
            else:
                maxi[nei] +=  maxi[node]

    else:
        for nei in adj[node]:
            maxi[nei]  = maxi[node] + time[nei-1]


print(maxi)
print(max(maxi.values()))