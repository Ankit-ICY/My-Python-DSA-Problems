def boolCheck(mid, threshold , nums):
    total = 0
    for i in range(len(nums)):
        if nums[i]%mid==0:
            total += nums[i]//mid

        else:
            total += ((nums[i]//mid)+1)


    if total<=threshold:
        return True
    return False


nums = [21212,10101,12121]

threshold = 1000000
s = 1
e = max(nums)


mid = s + (e-s)//2


while(s<=e):
    
    if boolCheck(mid, threshold , nums):
        e = mid - 1
    else:
        s = mid+1

    mid = s + (e-s)//2

print(s)