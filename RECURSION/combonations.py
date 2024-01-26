res =[]
ans =[]
def solve(nums,ind,k):
    if len(ans)==k:
        res.append(ans.copy())
        return ans


    

    for i in range(ind,n+1):
        ans.append(i)
        solve(nums,i+1,k)
        ans.pop()
        
    return res



n = 4
k = 2
nums =[]
for i in range(1,n+1):

    nums.append(i)
print(nums)
ind = 0
print(solve(n,1,k))