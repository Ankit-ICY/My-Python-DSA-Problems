s = "aaaa"
k = 2

dic = {}
ans = -1
i = 0
for j in range(len(s)):
    if s[j] not in dic:
        dic[s[j]] =1

    elif s[j] in dic:
        dic[s[j]] +=1

    if len(dic)>k:

        while(len(dic)>k):
            if s[i] in dic:
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]

            i+=1

    if len(dic)==k:
        ans = max(ans,j-i+1)

print(ans)