num = "1432219"
k = 1
n = len(num)
stack = []
for i in range(n):
    while(k!=0 and stack and int(num[i])<int(stack[-1])):
        stack.pop()
        k-=1
    if stack or num[i]!=0:
        stack.append((num[i]))
    
if k!=0:
    while(k!=0 and stack):
        stack.pop()

if stack:
    ans = ''.join(map(str,stack))
    print(ans)
