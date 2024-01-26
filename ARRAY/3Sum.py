nums = [-2,-3,0,0,-2]


nums.sort()
# [-4, -1, -1, 0, 1, 2]
n = len(nums)
ans = []
res = []

j = 1
k = n-1
i= 0
while(i<n-2):
    if j>=k:
        i +=1
        j= i+1
        k = n-1
        continue

    sum = nums[i] + nums[j] + nums[k]
    if sum== 0:
        ans.append(nums[i])
        ans.append(nums[j])
        ans.append(nums[k])
        res.append(ans.copy())
        ans.clear()
        k-=1
        j+=1
        while(j<k and nums[j]==nums[j-1]):j+=1
        while(j<k and nums[k]==nums[k+1]):k-=1

    elif sum>0:
        k-=1

    else:
        j+=1

    
print(res)