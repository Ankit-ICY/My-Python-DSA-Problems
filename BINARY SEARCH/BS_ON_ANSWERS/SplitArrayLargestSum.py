def possible(mid,nums,k , n):
    count = 1
    sum =0
    for i in range(n):
        if sum+nums[i]<=mid:
            sum+=nums[i]

        else:
            count+=1
            sum = nums[i]


    if count>k:
        return False
    return True
    

nums = [1, 1, 1, 1, 1, 1]
k = 2
n = len(nums)
s =max(nums)
e = sum(nums)

mid = s + (e-s)//2

while(s<=e):
    if possible(mid,nums,k , n):
        e = mid-1

    else:
        s = mid+1


    mid = s + (e-s)//2

print(s)
