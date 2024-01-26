nums = [4,-2,-3,4,1]
i = 0
j = 0
ans = 0
while(True):
    if j>=len(nums):
        i +=1
        j=i
    if i==len(nums):
        break


    ans+= max(nums[i:j+1]) - min(nums[i:j+1])
    j+=1

print(ans)