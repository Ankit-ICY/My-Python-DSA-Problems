s = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
stack = []

for i in range(len(s)):
    if s[i].lstrip('-').isdigit():
        stack.append(int(s[i]))
    else:
        b = stack.pop()
        a = stack.pop()

        if s[i] == '+':
            stack.append(a + b)
        elif s[i] == '-':
            stack.append(a - b)
        elif s[i] == '*':
            stack.append(a * b)
        elif s[i] == '/':
            stack.append(int(a / b))

ans = stack[0]

print(ans) 