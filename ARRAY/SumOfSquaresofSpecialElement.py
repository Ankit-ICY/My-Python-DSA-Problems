nums = [1,2,3,4]
n = len(nums)
sum = 0
for i in range(1,n+1):
    if n%i == 0:
        sum += (nums[i-1])**2

    
print(sum)