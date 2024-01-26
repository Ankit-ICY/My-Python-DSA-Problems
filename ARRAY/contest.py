

nums = [4,6,1,2]
k = 2
nums.sort()
n = len(nums)
left = 0
max_count = 1

for i in range(1,n):
    while(nums[left]+k<nums[i]-k):
        left += 1
        
    max_count = max(max_count,i-left+1)


print(max_count)