s = "(1+(2*3)+((8)/4))+1"
ans = 0
count = 0
for i in range(len(s)):
    if s[i] == '(':
        count+=1

    elif s[i] == ')' and count>0:
        count-=1

    ans = max(ans,count)


print(ans)