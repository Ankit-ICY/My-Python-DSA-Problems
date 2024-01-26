nums = [11,81,94,43,3]
i = 0
j = 0
ans = 0
while(True):
    if j >=len(nums):
        i +=1
        j=i
        if i==len(nums):
            break


    if i == j:
        mini = nums[j]
        


    while(j<len(nums) and  mini<=nums[j] ):
        ans+=mini
        j+=1

    if j<len(nums):
        mini = nums[j]
        ans +=mini
    else:
        continue

    j+=1
    
print(ans)