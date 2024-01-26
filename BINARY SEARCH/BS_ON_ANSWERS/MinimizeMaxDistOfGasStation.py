def boolCheck(mid,nums,k):
    count = 0
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1] <= mid:
            continue 
        else:
            count+= abs(nums[i]-nums[i-1]) // mid
            if  count>k:
                return False

    return True


nums = [3,6,12,19,33,44,67,72,89,95]
k = 2
n = 10
s = 0
e = nums[-1] - nums[0]

ans = 0
while(e - s> 10**-2):
    mid = s + (e-s)/2.0
    if boolCheck(mid,nums,k):
        ans = mid
        e = mid
    else:
        s =mid
print(ans)

