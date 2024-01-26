s = "()))(("

op = 0
close = 0
for i in range(len(s)):
    if s[i] == "(":
        op+=1
        

    elif s[i] == ")":
        if op>0:
            op-=1

        else:
            close+=1

    

print(op + close)
