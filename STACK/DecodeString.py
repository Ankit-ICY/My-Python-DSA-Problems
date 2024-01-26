s =  "2[abc]3[cd]ef"

stack = []
for i in s:
    
    if i == "]":
        temp = ""
        while stack and stack[-1] != "[":
            temp =stack.pop() + temp
        stack.pop()
        num = ""

        while stack and stack[-1].isdigit():
            num=stack.pop() + num

        stack.append( int(num) * temp )

    
    else:
        stack.append(i)


ans = ''.join(map(str, stack))

print(ans)