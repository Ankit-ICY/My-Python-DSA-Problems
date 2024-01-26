def opCheck(op):
    if op=='^':
        return 3
    
    elif op=="*" or op == "/":
        return 2

    elif op == "+" or op == '-':
        return 1

    else:
        return -1

s = "a+((b*c)*d)&e"
stack = []
string =""
for i in range(len(s)):
    if s[i].isalpha() or s[i].isdigit() :
        string+=s[i]


    elif s[i] == "(":
        stack.append(s[i])


        
    elif s[i] == ")":
        while(stack and stack[-1]!= "("):
            string+=stack[-1]
            stack.pop()

        if len(stack)>0:
            stack.pop()

    else:
        while(stack and opCheck(s[i])<opCheck(stack[-1])):
            string+=stack[-1]
            stack.pop()

        stack.append(s[i])



while(stack):
    string+=stack[-1]
    stack.pop()


print(string)