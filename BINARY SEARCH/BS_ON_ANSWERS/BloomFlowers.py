def BloomBloom(mid, nums, m , k):
    count = 0
    bouquets  = 0
    for i in range(len(nums)):
        if nums[i]<=mid:
            count+=1

        else:
            bouquets+= (count//k)
            count = 0

    bouquets+=(count//k)
    if bouquets>=m:
        return True
    return False


nums = [7,7,7,7,12,7,7]
m = 2
k = 3

s = min(nums)
e = max(nums)

while(s<=e):
    mid = s + (e-s)//2
    if BloomBloom(mid, nums, m , k):
        e = mid-1

    else:
        s = mid+1


print(s)
