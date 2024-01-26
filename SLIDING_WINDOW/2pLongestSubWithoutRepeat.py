s = "ohvhjdml"
i = 0
j = 0
set = []
ans = 0
while(j<len(s)):
    if s[j] not in set:
        set.append(s[j])
    else:

        while(len(set)!=0 and set[0] != s[j]):
            i+=1
            set.pop(0)
            
        set.pop(0)
        i+=1
        set.append(s[j])

    j+=1
    ans = max(ans,len(set))


print(ans)