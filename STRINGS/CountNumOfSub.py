s = "abaaca"
k = 1
d = {}

ans =0 
for i in range(len(s)):

    d = {}
    j = i
    while(j<len(s)):


        if s[j] in d:
            d[s[j]]+=1
        else:
            d[s[j]] = 1

        if  len(d)==k:
            ans+=1
        
        j+=1   

print(ans)