arr = [11,81,94,43,3]
stack = []
n = len(arr)
prev = [0]*n
next = [0]*n
ans = 0
for i in range(n):
    j=i
    while(stack and stack[-1]>=arr[i]):
        stack.pop()
        j-=1

    if stack:
        prev[i] = i-j
    else:
        prev[i] = i


    stack.append(arr[i])

stack = []
for i in range(n-1,-1,-1):
    j = i
    while(stack and stack[-1]>=arr[i]):
        stack.pop()
        j+=1
    
    if stack:
        next[i] = j-i
    else:
        next[i] = n-i-1

    stack.append(arr[i])

ans = 0
for i in range(n):
    ans+=arr[i] *  (prev[i] + 1 )* (next[i] + 1)
    
print(prev)
print(next)
# print(ans)