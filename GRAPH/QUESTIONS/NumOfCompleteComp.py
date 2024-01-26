def  check(curr , edges):
    for i in range(len(cur)):
        for j in range(i+1, len(curr)):
            u = min(curr[ i] , curr[j])
            v = max(curr[i] , curr[j])

            if [u,v] not in edges:
                return False

    return True

def solve(visited,node ,ans):
    q = [node]

    while(q):
        v = q.pop(0)

        for i in adj[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i) 
                cur.append(i)

        
    if check(cur , edges):
        ans +=1


n = 6
edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
adj = [[]for _ in range(n)]
for i  in range(len(edges)):
    u = edges[i][0]
    v = edges[i][1]
    adj[u].append(v)

cur =[]
ans = 0
visited = [False]*n
count = 0
for  i in range(n):
    if not visited[i]:
        visited[i] = True
        count+=1
        cur.append(i)
        solve(visited,i,ans)


print(ans)