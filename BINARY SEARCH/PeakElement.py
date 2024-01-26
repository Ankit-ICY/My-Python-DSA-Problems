nums = [1,2,1,2,1]

s = 0
e = len(nums)-1
mid = s + (e-s)//2

while(s<=e):
    if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
        print(mid)
        break

    elif nums[mid]>nums[mid-1]:
        s = mid+1

    else:
        e = mid-1
    
    mid = s + (e-s)//2


