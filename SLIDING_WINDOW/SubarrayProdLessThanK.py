nums = [1,1,1]
k = 1

sum = 1
ans = 0
i = 0
cnt = 0
for j in range(len(nums)):
    sum *= nums[j]


    while sum>=k and i <=j :

        sum//= nums[i]
        i+=1


    ans+= j-i+1



print(ans)