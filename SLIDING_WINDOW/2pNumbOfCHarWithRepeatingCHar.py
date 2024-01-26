s = "abcabc"
temp  = "abc"
from collections import Counter
dic = Counter(temp)
count = len(dic)
ans = 0
i = 0
c = 0
for j in range(len(s)):
    if s[j] in dic:
        dic[s[j]]-=1
        if dic[s[j]] == 0:
            count-=1

    if count == 0:
        while(count==0):
            c+=1
            if s[i] in dic:
                dic[s[i]]+=1
                if dic[s[i]]>0:
                    
                    count+=1
            i+=1

    ans+=c


print(ans)