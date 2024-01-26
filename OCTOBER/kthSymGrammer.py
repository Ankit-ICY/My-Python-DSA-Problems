def solve(n,k,s):
    if n==1:
        return s
    
    string =""
    for i in range(len(s)):
        if s[i] == "0":
            string+='01'

        else:
            string+="10"

    return solve(n-1,k,string)

        
n = 30
k = 3
s = "0"

print(solve(n,k,s))