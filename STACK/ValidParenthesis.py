s = "(){}}{"
op = "({["
cl = ")}]"
stack = []
for i in range(len(s)):
    if s[i] in op:
        stack.append(s[i])

    else:
        ind = cl.index(s[i])
        if stack and stack[-1] == op[ind]:
            stack.pop()
        else:
            stack.append(s[i])

print(stack)
