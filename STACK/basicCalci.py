def opCheck(op):
    if op=="^":
        return 3
    
    elif op=="*" or op=="/":
        return 2

    elif op == "-" or op == "+":
        return 1

    else:
        return -1

s ="1-(-2)"


stack = []
string = ""
i = 0
while i<len(s):
    if s[i].isdigit():
        temp = ""
        while i<len(s) and s[i].isdigit():
            temp += s[i]
            i+=1
        string += temp  + ','

    elif s[i] == "(":
        stack.append(s[i])
        i+=1

    elif s[i] == ")":
        while(stack and stack[-1]!= "("):
            string+=stack[-1] + ','
            stack.pop()

        if len(stack)>0:
            stack.pop()

        i+=1


    elif s[i] == " ":
        i+=1
        continue
    

    else:
        while stack and opCheck(s[i]) <= opCheck(stack[-1]):
            string += stack[-1] + ','
            stack.pop()

        stack.append(s[i])
        i+=1

while stack:
    string += stack.pop() + ","


string = string[:-1]
# print(string)

s = string.split(',')

print(s)
for i in range(len(s)):
    if s[i].isdigit():
        stack.append(s[i])

    elif s[i] ==",":
        continue

    else:
        a = 0
        b = 0
        if stack:
            b = stack.pop()
        if stack:
            a = stack.pop()

        if s[i] == "/":
            stack.append( int(a)//int(b)  )
        elif s[i] == "*":
            stack.append( int(a)*int(b)  )
        elif s[i] =="+":
            stack.append( int(a)+int(b)  )
        else:
            stack.append( int(a)-int(b)  )
    

ans = stack[0]

print(ans)
