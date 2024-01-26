nums = [1,3,8,48,10]
num = 0
j=0
count = 0
for i in range(len(nums)):

    while num & nums[i] != 0:
        num ^= nums[j]
        j+=1
    
    num |= nums[i]
    count = max(count , i-j+1)

print(count)

