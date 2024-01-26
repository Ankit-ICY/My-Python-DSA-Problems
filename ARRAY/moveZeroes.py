nums = [0]

n = len(nums)
i = 0
j= 1

while(j<n):
    if nums[i] == 0 and nums[j]!=0:
        nums[i] = nums[j]
        nums[j] = 0
        i+=1
        j+=1
    
    elif nums[i]!=0:
        i+=1
        j+=1
        
    elif nums[j] == 0:
        j+=1

    

print(nums)