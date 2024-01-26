def MaxCards(nums,i,j,dp,k):
    if k==0 or i>j:
        return 0


    x1 = nums[i]  + MaxCards(nums,i+1,j,dp,k-1)
    x2 = nums[j] +  MaxCards(nums,i,j-1,dp,k-1)
    x= max(x1,x2)


    return x

nums =  [9,7,7,9,7,7,9]
k = 7
i  = 0
j = len(nums)-1
dp ={}
print(MaxCards(nums,i,j,dp,k))

