def PalindromePart(s,ans,res,ind):
    if ind==len(s):
        res.append(ans.copy())
        return


    string = ""
    for i in range(ind,len(s)):
        string+=s[i]
        if string == string[::-1]:
            ans.append(string)
            PalindromePart(s,ans,res,i+1)
            ans.pop()
    
    return res


s = "ababbbabbababa"
ans = []
res = []
ind = 0
print(PalindromePart(s,ans,res,ind))