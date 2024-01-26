s = "abaacbabc"
p = "abc"

from collections import Counter

dic = Counter(p)


i = 0
ans = []
count = len(dic)
for j in range(len(s)):
    
    if s[j] in p:
        dic[s[j]] -=1

        if dic[s[j]] == 0:
            count-=1

    if count == 0:

        while count == 0:
            if s[i] in p:
                dic[s[i]] +=1
                if dic[s[i]]>0:
                    count+=1
                    if j-i+1==len(p):
                        ans.append(i)
            i+=1


print(ans)