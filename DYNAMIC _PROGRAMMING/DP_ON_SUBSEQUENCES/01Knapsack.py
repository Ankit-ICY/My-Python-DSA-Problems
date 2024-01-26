def solve(weight,values,ind,n,w,dp):
    if w==0 or ind==n:
        return 0
    # if ind==n:
    #     return 0
    
    if weight[ind]<=w:
        x1 = values[ind] + solve(weight,values,ind+1,n,w-weight[ind],dp)
        x2 = solve(weight,values,ind+1,n,w,dp)
        x = max(x1,x2)

    else:
        x = solve(weight,values,ind+1,n,w,dp)
        

    return x


values = [1,2,3]
weight = [4,5,6]
w = 3
n= 3
ind = 0 
dp ={}
print(solve(weight,values,ind,n,w,dp))