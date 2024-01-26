def FindParent(node):
    if parent[node] == node:
        return node

    else:
        parent[node] = FindParent(parent[node])
        return parent[node]

def disjoint(u,v):
    extra = 0
    ul_u = FindParent(u)
    ul_v = FindParent(v)
    if ul_u == ul_v:
        extra +=1

    if size[ul_v]> size[ul_u]:
        parent[ul_u] = ul_v
        size[ul_v] += size[ul_u]
    else:
        parent[ul_v] = ul_u
        size[ul_u] += size[ul_v]

    return extra

n = 6

connections = [[0,1],[0,2],[0,3],[1,2]]

size = [1]*n
parent = [0]*n
for i in range(n):
    parent[i] = i

ex = 0
for i in connections:
    ex +=disjoint(i[0] , i[1])

count = 0
for i in range(n):
    if parent[i] == i :
        count+=1
    
edge = count-1

if ex>=edge:
    print(edge)

else:
    print(-1)