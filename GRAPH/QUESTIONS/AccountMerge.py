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
        return

    if size[ul_v]> size[ul_u]:
        parent[ul_u] = ul_v
        size[ul_v] += size[ul_u]
    else:
        parent[ul_v] = ul_u
        size[ul_u] += size[ul_v]


accounts = [ ["John","johnsmith@mail.com","john_newyork@mail.com"]
            ,["John","johnsmith@mail.com","john00@mail.com"]
            ,["Mary","mary@mail.com"]
            ,["John","johnnybravo@mail.com"] ]



n = len(accounts)
size = [1]*n
parent = [0]*n
for i in range(n):
    parent[i] = i
mails = {}
for i in range(0, n):
    for j in range(1,len(accounts[i])):
        mail =accounts[i][j]
        if mail not in mails:
            mails[mail] = i
            size[i]+=1
        else:
            disjoint(i , mails[mail] )



mergeMail = [[] for _ in range(n)]
for i , j in mails.items():
    ul = parent[j]
    mergeMail[ul].append(i)

ans = []
for i in range(n):
    if not mergeMail[i]:continue
    a = []
    a.append(accounts[i][0])
    for j in (mergeMail[i]):
        a.append(j)

    ans.append(a)

print(ans)