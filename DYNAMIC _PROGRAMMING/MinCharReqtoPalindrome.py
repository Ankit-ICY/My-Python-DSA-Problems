def solve(s,i,j,dp):
    if i>=j:
        return 0
    

    if s[i] == s[j]:
        x1 = solve(s,i+1,j-1,dp)
        x2 = 1 + solve(s,i,j-1,dp)
        x = min(x1,x2)

    else:
        x = 1 + solve(s,i,j-1,dp)


    return x

s = "hqghumeaylnlfdxfi"
i =0
j = len(s)-1
dp ={}

print(solve(s,i,j,dp))
