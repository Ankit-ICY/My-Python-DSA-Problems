def bubbleSorting(nums,n):
    if n==1:
        return 
    
    count = 0

    for i in range(n-1):
        if nums[i]>nums[i+1]:
            count+=1
            nums[i] , nums[i+1] = nums[i+1] ,nums[i]

    if count == 0:
        return     
    
    bubbleSorting(nums,n-1)


nums = [64, 34, 25, 12, 22, 11, 90]
n = len(nums)

bubbleSorting(nums,n)

print(nums)