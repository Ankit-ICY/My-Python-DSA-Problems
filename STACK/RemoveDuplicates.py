s = "wilddddddddddgooowwwwwwwwwwoooossssssssssoccccccchhhhhhhhhhcccccccccccccooryyyyyyyffffffffffyyynaicv"
k = 4
stack =[]
dic ={}

for i in range(len(s)):
    
    if stack and s[i] == stack[-1] and i+1 < len(s) and s[i] != s[i+1]:
        x = len(stack)-1
        count=0
        while  x>=0 and stack[x] == s[i]:  
            count +=1
            x-=1
        
        if count >=k-1:
            x = k-1
            while stack and x:
                stack.pop()
                x-=1
        else:
            stack.append(s[i])
             
    else:    
        stack.append(s[i])

  
x = len(stack)-1
while  x>=0 and stack[x] == s[i]:  
    count +=1
    x-=1

if count >=k:
    x = k
    while stack and x:
        stack.pop()
        x-=1

ans = ''.join(map(str,stack))
print(ans)