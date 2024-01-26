s = "(()(()))"

stack = []
flag = 0
count = 0
for i in range(len(s)):
    if s[i]=="(":
        stack.append("(")
        

    elif s[i] == ")":
        if  stack[-1] == "(":
            stack.pop()
            if not stack or  stack[-1]=="(":
                stack.append(1)
            elif stack and stack[-1] != "(": 
                stack[-1] += 1

        elif stack and stack[-1]!= '(':
            temo = 2 * stack.pop()
            stack.pop()
            if not stack or  stack[-1]=="(":
                stack.append(temo)
            else:
                stack[-1] += temo
        

print(stack)