s = "aabc"
q = []
ans = ""
count = {}
for i in range(len(s)):
    count[s[i]] = 0


for i in range(len(s)):
    char = s[i]

    count[char] +=1
    q.append(char)
    while q:
        if count[q[0]]>1:
            q.pop(0)

        else:
            ans+=q[0]
            break

    if not q:
        ans+='#'


print(ans)