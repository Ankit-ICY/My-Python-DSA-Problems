s =  "(a+b)/(c-d)+e*f/g"

stack = []

for i in range(len(s)):
    if s[i].isdigit() :
        stack.append(s[i])

    else:
        k = 2
        a = ""
        b = ""
        while stack and k!=0:
            if not b:
                b+=stack.pop()
                k-=1

            elif not a:
                a+=stack.pop()
                k-=1

        stack.append('('+ a + s[i] + b+ ')')

print(stack[0])
