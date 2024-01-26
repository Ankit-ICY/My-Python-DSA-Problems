times = [[1,2,1],[2,3,7],[1,3,4],[2,1,2]]
n = 3
k = 2

adj = {}
adj = [[] for _ in range(n+1)]

for i in range(len(times)):
    u = times[i][0]
    v = times[i][1]
    w = times[i][2]

    adj[u].append([v,w])
print(adj)

distance = [1e9]*(n+1)
distance[k] = 0

q = [[0, k]]

while q:
    node = q.pop(0)
    signal = node[0]
    vertex = node[1]

    for i in adj[vertex]:
        v = i[0]
        w = i[1]

        if w  + signal < distance[v]:
            distance[v] = signal + w
            q.append([signal + w , v])

print(distance)