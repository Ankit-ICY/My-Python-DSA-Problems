def palindromePart(ind,s,dp):
    if ind >=len(s):
        return 0

    string = ""    
    mini = 1e9

    for i in range(ind,len(s)):
        string+=s[i]
        if string==string[::-1]:
            mini = min(mini, 1 + palindromePart(i+1,s,dp))
            
        
    return mini

s = "ababbbabbababa"
ind = 0
print(palindromePart(ind,s,{})-1)
