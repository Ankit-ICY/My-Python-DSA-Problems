def solve(ind,dp,ans,s ,string ):
   
    if string not in ans:
        ans.append(string)

    string =""

    for i in range(ind,len(s)):
        string+=s[i]
        solve(i+1,dp,ans,s,string)
 
    return len(ans)



s = "abc"
ind= 0
dp ={}
ans =[]
print(solve(ind,dp,ans,s, ""))