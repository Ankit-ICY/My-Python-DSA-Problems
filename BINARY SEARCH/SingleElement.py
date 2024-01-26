nums = [7,7,10,11,11,12,12]
n = len(nums)
if nums[0]!=nums[1]:
    print(nums[0])
if nums[n-1] != nums[n-2]:
    print(nums[n-1])

s = 1
e = len(nums)-2
mid = s + (e-s)//2

while(s<=e):
    if nums[mid]!=nums[mid-1] and nums[mid]!= nums[mid+1]:
        print(nums[mid])
        break

    elif (mid%2==1 and nums[mid]==nums[mid+1]) or (mid%2 ==0 and nums[mid]==nums[mid-1]):
        e = mid-1

    else:
        s = mid+1

    mid = s + (e-s)//2

