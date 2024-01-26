s = "abcdebdde"
t = "bde"

from collections import Counter

dic = {}
dic = Counter(t)
j = len(s)-1
map = {}
count = len(dic)
x = 0
ind = 0
ans = 1e9
for i in range(len(s)):

    if s[i] in t:
        dic[s[i]]-=1
        if dic[s[i]]==0:
            count-=1

    if count==0:        
        while(count==0):
            if i-x+1 <ans:
                ans = i-x+1
                ind = x
            if s[x] in dic:
                dic[s[x]] +=1
                if dic[s[x]]>0:
                    count+=1

            x+=1

print(s[ind:ind+ans])


1401012192
2002003457