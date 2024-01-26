grid = [  [0,1,0]
        , [0,0,0]
        , [0,1,0] ]

n = 3
stack = []

for  i in range(n):
    stack.append(i)


while(len(stack)>1):
    a = stack[-1]
    stack.pop()

    b = stack[-1]
    stack.pop()

    if grid[a][b]==1:
        stack.append(b)
    else:
        stack.append(a)


celeb = stack[0]
countR = 0
for i in range(n):
    if grid[celeb][i]==0:
        countR+=1


countC = 0
for i in range(n):
    if grid[i][celeb]==0:
        countC+=1


if countR == n and countC==n-1:
    print(celeb)
else:
    print(-1)