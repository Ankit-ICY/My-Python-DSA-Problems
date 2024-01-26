def solve(nums,n,prev,ind,dp):
    if ind==n-1:
        return 0

    mini = 1e9

    for i in range(ind+1,min(n ,ind+ nums[ind]+1)):
        # if nums[i] >=nums[prev]:
        mini = min(mini,1 + solve(nums,n,i,i,dp))


    return mini


nums = [2 ,3 ,1 ,1 ,2 ,4 ,2, 0 ,1 ,1]
n =10
prev = 0
ind = 0
dp ={}
print(solve(nums,n,prev,ind,dp))


# 2 ,3 ,1 ,1 ,2 ,4 ,2, 0 ,1 ,1

# 1 3 5 8 9 2 6 7 6 8 9