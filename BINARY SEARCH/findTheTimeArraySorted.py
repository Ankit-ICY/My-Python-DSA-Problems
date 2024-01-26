nums = [4,5, 1, 2, 3]
n = 5
s = 0
e = n-1
mid = s + (e-s)//2
ans = 1e9
ind  = -1
while(s<=e):
    if nums[s] <nums[e]:
        if nums[s]<ans:
            ind = s
            ans = nums[s]
        break


    if nums[s]>nums[mid]:
        if  nums[mid]<ans:
            ans = nums[mid]
            ind = mid

        e = mid-1
    else:
        if nums[s]<ans:
            ans = nums[s]
            ind = s

        s = mid+1

    mid = s + (e-s)//2

print(ind)


    