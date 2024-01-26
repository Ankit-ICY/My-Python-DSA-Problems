def solve(nums,k,ind,dp,prev):
    if ind>=len(nums):
        return nums[prev]
    

    x = 0

    if  ((nums[prev]%2==0 and nums[ind]%2==0 ) or (nums[prev] %2==1 and nums[ind] %2 == 1)) :
        x1 = nums[prev]  + solve(nums,k,ind+1,dp,ind)
        x2 = solve(nums,k,ind +1 ,dp,prev)
        x = max(x1,x2)


    elif ((nums[prev]%2==1 and nums[ind]%2==0 ) or (nums[prev] %2==0 and nums[ind] %2 == 1)):
        x1 =   (nums[prev]-k) +    solve(nums,k,ind+1,dp,ind)
        x2 = solve(nums,k,ind+1,dp,prev)
        x = max(x1,x2)

    
    # else : 
    #     x = solve(nums,k,ind+1,dp,prev)


        
    return x

nums =   [2,3,6,1,9,2]
x = 5
prev = 0
ind = 1
dp ={}
print(solve(nums,x,ind,dp,prev))