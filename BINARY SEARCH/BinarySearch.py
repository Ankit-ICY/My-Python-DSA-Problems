nums = [1,3,5,6]
target = 7
s = 0
e = len(nums)-1
mid = s + (e-s)//2

while(s<=e):
    if nums[mid] == target:
        print(mid)
        break

    elif nums[mid]> target:
        e = mid -1

    else:
        s = mid+1

    mid = s + (e-s)//2
    
