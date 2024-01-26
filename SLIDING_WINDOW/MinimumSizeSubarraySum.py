target = 11
nums =[1,2,3,4,5]



i  = 0
sum = 0
ans = 1e9
for j in range(len(nums)):
    sum += nums[j]


    while sum>=target:
        if sum == target:
            ans = min(ans, j-i + 1)
        

        sum-=nums[i]
        i+=1

print(ans)