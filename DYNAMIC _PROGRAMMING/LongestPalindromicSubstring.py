s = "mixrpifeffeclhbvfukbyeqfqo"


maxi = 0
ans = ""
for k in range(len(s)):
    
    # ODD

    i = k-1
    j = k+1
    count = 1
    while i>=0 and j<len(s) and s[i] == s[j]:
        i-=1
        j+=1
        count+=2

    if count>maxi :
        ans = s[i+1 : j] 
        i+=1
        maxi = j-i

    
    # EVEN

    i=k
    j = k+1
    count = 0
    
    while i>=0  and j<len(s) and s[i] == s[j]:
        count+=2
        i-=1
        j+=1

    if count>maxi :
        ans = s[i+1 : j] 
        i+=1
        maxi = j-i

    

print(ans)