s = "aabcbaa"
d = {}
ans =0 
for i in range(len(s)):
    if s[i] in d:
        d[s[i]]+=1
    else:
        d[s[i]] = 1
    j = i+1
    while(j<len(s)):
        if s[j] in d:
            d[s[j]]+=1
        else:
            d[s[j]] = 1
            
        ans += max(d.values()) - min(d.values())
        j+=1    
    d = {}


print(ans)