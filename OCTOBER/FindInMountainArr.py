nums = [3,5,3,2,0]
target = 0

s = 1
e = len(nums)-2

while s<=e:
    mid = s + (e-s)//2
    el = nums[mid]
    if el > nums[mid-1] and el> nums[mid+1]:
        e= mid
        p = mid
        break

    elif el >nums[mid-1]  and el<  nums[mid+1]:
        s = mid+1

    else:
        e = mid-1

s = 0

while s <=e:
    mid = s + (e-s)//2
    el = nums[mid]
    if el == target:
        print( mid)
        break
    
    elif target < el:
        e = mid-1
    else:
        s = mid+1

s = p
e = len(nums)-1
while s<=e:
    mid = s + (e-s)//2
    el = nums[mid]
    if el == target:
        print(mid)
        break
    
    elif target < el:
        s = mid+1
    else:
        e = mid-1






print(-1)
