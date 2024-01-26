def solve(s1,s2,i,j,dp):
    if i>=len(s1) or j>=len(s2):
        return 0

    if s1[i] == s2[j] :
        x = solve(s1,s2,i+1,j+1,dp)

    else:
        x1 = solve(s1,s2,i+1,j,dp)
        x2 =solve(s1,s2,i,j+1,dp)
        x  = min(x1,x2)

    return x

s1 = "ABCDGH"
s2=  "AEDFHR"

i = 0
j = 0

dp ={}
print(solve(s1,s2,i,j,dp))