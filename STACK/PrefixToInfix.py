s = "*-A/BC-/AKL"
stack = []

for i in range(len(s)-1 , -1 , -1):
    if s[i].isalpha() :
        stack.append(s[i])

    else:
        k = 2
        a = ""
        b = ""
        while stack and k!=0:
            if not a:
                a+=stack.pop()
                k-=1

            elif not b:
                b+=stack.pop()
                k-=1

        stack.append('('+ a + s[i] + b+ ')')

print(stack[0])
