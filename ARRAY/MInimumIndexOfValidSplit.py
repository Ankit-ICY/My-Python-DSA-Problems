def check(mid , nums):
    max1 = max(set(nums[0:mid+1]), key = nums[0:mid+1].count)
    max2 = max(set(nums[mid+1:]), key = nums[mid+1:].count)

    if max1 == max2:
        count1 = 0
        for i in range(mid+1):
            if nums[i]==max1:
                count1+=1

        count2 = 0
        for i in range(mid+1, len(nums)):
            if nums[i]==max2:
                count2 +=1

        
        if count1 * 2 > mid+1 and count2 * 2 > (len(nums)-(mid+1)):
            return True
        
    return False


nums = [1,1,1,2]
s = 0
e = len(nums)-2
ans = -1
while( s<=e) :
    mid = s  + (e-s)//2


    if check(mid , nums):
        ans = mid
        e  = mid-1

    else:
        s = mid+1

print(ans) 