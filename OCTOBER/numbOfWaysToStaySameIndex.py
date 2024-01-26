def solve(step, n,ind):
    if ind>=n or ind<0 or step>steps:
        return 0
    

    if  step==steps and ind==0:
        return 1


    right = solve(step+1, n,ind+1)
    left = solve(step+1, n,ind-1)
    stay = solve(step+1, n,ind)
    x = (right + left + stay)%mod

    return x


steps  = 4
n = 2
mod = 1000000000 + 7
print(solve(0, n , 0))