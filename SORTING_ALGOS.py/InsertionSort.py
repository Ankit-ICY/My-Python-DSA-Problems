nums = [12, 31, 25, 8, 32, 17]
n = len(nums)

for i in range(n-1):
    if nums[i]>nums[i+1]:
        nums[i] , nums[i+1] = nums[i+1] , nums[i]
        j = i
        
        while (j>0 and  nums[j]<nums[j-1]):
            nums[j] , nums[j-1] = nums[j-1] , nums[j]
            j-=1
            


print(nums)