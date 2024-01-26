garbage = ["MMM","PGM","GP"]
travel = [3,10]
g = 0
m = 0
p = 0

n = len(travel)
prefix = [0]*n
for i in range(n):
    prefix[i] = travel[i]+ prefix[i-1]

ans = 0

for i in range(len(garbage)):
    x = garbage[i]
    if 'G' in x:
        g = i
    if 'M' in x:
        m = i
    
    if 'P' in x:
        p = i

    ans+= len(x)


if g>=1: ans+=prefix[g-1]
if p>=1: ans+=prefix[p-1]
if m>=1: ans+=prefix[m-1]

print(ans)

