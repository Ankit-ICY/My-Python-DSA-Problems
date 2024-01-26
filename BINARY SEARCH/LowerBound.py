nums = [1,2,8,10,11,12,19]
n = 7
x = 5
s = 0
e = len(nums)-1
mid = s + (e-s)//2

while(s<=e):
    if nums[mid] == x:
        # print(mid)
        break

    elif nums[mid]> x:
        e = mid -1

    else:
        s = mid+1

    mid = s + (e-s)//2
    
print(s)