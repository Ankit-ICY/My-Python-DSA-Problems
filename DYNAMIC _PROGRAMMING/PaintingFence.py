
def solve(n,k,change,ind):

    if n == 0:
        return 1

    if k==0:
        return 0

    if change>0:
        x1= solve(n-1,k,change-1,ind)
        x2 = solve(n,k-1,2,ind)
        x = x1 + x2

    else:
        x = solve(n,k-1,2,ind)


    return x


n = 3
k =2

print(solve(n,k,2,0))