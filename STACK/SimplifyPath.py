s = "/../"


i  = 0
stack = []
while i<len(s):

    if s[i]=="/":
        i+=1
        continue
    else:
        temp = ""
        while  i<len(s) and s[i]!="/":
            temp+=s[i]
            i+=1

        if temp == "..":
            if stack:
                stack.pop()
            else:
               continue

        elif temp==".": 
            continue
        else:
            stack.append(temp)


ans = '/'.join(map(str, stack))
ans = "/" + ans 
print(ans)
