def solve(i,s,j,dp):
    if i==j:
        return 1
    
    if  i>j:
        return 0


    if s[i] == s[j]:
        x1= 1 + solve(i+1,s,j,dp)
        x2 = solve(i,s,j-1,dp)
        x = x1 + x2
 
    else:
        x1 = solve(i+1,s,j,dp)
        x2 = solve(i,s,j-1,dp)
        x3 = solve(i+1,s,j-1,dp)
        x= x1  +x2 - x3

    return x


s = "aaaa"

ind = 0
j = len(s)-1
dp = {}
print(solve(ind,s,j,dp))