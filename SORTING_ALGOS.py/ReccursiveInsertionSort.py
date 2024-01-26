def insert(nums,ind,n):
    
    while (ind>0 and  nums[ind]<nums[ind-1]):
        nums[ind] , nums[ind-1] = nums[ind-1] , nums[ind]
        ind-=1
        

    return 
            


def InsertionSorting(nums,n,i):
    
    if i==n-1:
        return 

    if nums[i]>nums[i+1]:
        nums[i] , nums[i+1] = nums[i+1] , nums[i]
        insert(nums,i,n)

    
    InsertionSorting(nums,n,i+1)


nums = [12, 31, 25, 8, 32, 17]
n = len(nums)
i = 0
InsertionSorting(nums,n,i)

print(nums)