def opCheck(op):
    if op=="^":
        return 3
    
    elif op=="*" or op=="/":
        return 2

    elif op == "-" or op == "+":
        return 1

    else:
        return -1

s = "(1+(4+5+2)-3)+(6+8)"

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

print(string)
string = string[:-1]
s = string.split(',')
# s = string

print(s)



for i in range(len(s)):
    if s[i].isdigit():
        stack.append(s[i])

    elif s[i] ==",":
        continue

    else:

        b = stack.pop()

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
