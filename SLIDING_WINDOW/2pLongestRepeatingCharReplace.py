s = "AABBAAA"
k = 1
dic = {}

i = 0
ans = 0
for j in range(len(s)):
    if s[j] not in dic:
        dic[s[j]] = 1

    elif s[j] in dic:
        dic[s[j]] +=1


    if j-i+1 - max(dic.values())  > k:
        dic[s[i]]-=1
        i+=1

    ans = max(ans,j-i+1)

print(ans)