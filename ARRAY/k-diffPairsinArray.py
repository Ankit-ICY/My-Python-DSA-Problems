nums  = [3,1,4,1,5]
k = 2
nums.sort()

i = 0
j = 1
ans = []
while(j<len(nums)):
    diff = nums[j] - nums[i]
    if diff== k:
        if [nums[j] , nums[i]] not in ans:
            ans.append([nums[j] , nums[i]])
        i+=1
        j+=1
    elif diff>k:
        i+=1
    else:
        j+=1

    if i==j:
        j+=1

print(len(ans))