def maxCards(nums,i,j,k,dp):
    if i>j :
        return 0

    elif (i,j) in dp:
        return dp[(i,j)]
    
    
    for x in range(k):
        dp[(i,j)] = max(nums[j]+ maxCards(nums,i,j-1,k,dp), nums[i] +  maxCards(nums,i+1,j,k,dp))

    return dp[(i,j)]



nums =[9,7,7,9,7,7,9]
k = 7
i = 0
j = len(nums)-1

print(maxCards(nums,i,j,k,{}))