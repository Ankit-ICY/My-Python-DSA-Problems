s = "(()))())("
stack = []

ans = 0
count = 0
for i in range(len(s)):

    if stack and s[i] == ")" :
        if stack[-1]=="(":
            stack.pop()
            if stack and stack[-1] != "(" and stack[-1] !=")":
                stack[-1] = stack[-1] + 2
            else:
                stack.append(2)

        elif stack[-1] == ")":
            stack.append(s[i])

        else:
            num = stack.pop()
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                    cnt = 0
                    while stack and stack[-1] != ")" and stack[-1] !="(":
                        cnt+=stack.pop()
                    stack.append(cnt +num+ 2)
                else:
                    stack.append(num)
                    stack.append(s[i])
            else:
                stack.append(num)
                stack.append(s[i])


    else:
        stack.append(s[i])


print(stack)
ans = 0
for i in stack:
    if i!=')' and i!="(":
        ans = max(ans,i)

print(ans)