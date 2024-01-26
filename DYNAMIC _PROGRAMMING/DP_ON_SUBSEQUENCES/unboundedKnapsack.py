def solve(weight,values,ind,n,w,dp):
    if w==0 or ind==n:
        return 0
    # if ind==n:
    #     return 0
    
    if weight[ind]<=w:
        x1 = values[ind] + solve(weight,values,ind,n,w-weight[ind],dp)
        x2 = solve(weight,values,ind+1,n,w,dp)
        x = max(x1,x2)

    else:
        x = solve(weight,values,ind+1,n,w,dp)
        

    return x


values = [1, 4, 5, 7]
weight = [1, 3, 4, 5]
w = 8
n= 4
ind = 0 
dp ={}
print(solve(weight,values,ind,n,w,dp))