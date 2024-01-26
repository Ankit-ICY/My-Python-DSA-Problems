s = "ABC/-AK/L-*"

stack = []

for i in range(len(s)):
    if s[i].isalpha() :
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

        stack.append(s[i] + a + b)

print(stack[0])
