nums = [3,1,3,4,2]


nums.sort()
s = 0
e = len(nums)-1
ans= 0
while s<=e :

    mid= s + (e-s)//2

    if nums[mid]==mid+1:
        s = mid+1

  
    else:
        ans = nums[mid]
        e = mid-1

print(ans)