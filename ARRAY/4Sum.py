nums = [10,2,3,4,5,7,8]
target = 23
nums.sort()
ans = []
res = []
n = len(nums)
l = n-1
for i in range(n-3):
    if i>0 and nums[i] == nums[i-1]:continue
    for j in range(i+1,n-2):
        if j>i+1 and nums[j]==nums[j-1]:continue
        k  = j+1
        l = n-1
        while(k<l):

            sum = nums[i] + nums[j] + nums[k] + nums[l]

            if sum == target:
                ans.append(nums[i])
                ans.append(nums[j])
                ans.append(nums[k])
                ans.append(nums[l])
                if ans not in res:
                    res.append(ans.copy())
                ans.clear()
                k+=1
                l-=1
                while(k<l and nums[k] == nums[k-1]):k+=1
                while(k<l and nums[l] == nums[l+1]) : l-=1



            elif target>sum:
                k+=1
            
            else:
                l-=1


print(res)