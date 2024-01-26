nums = [1,2,3,2]
k = 1

s = 0
e = len(nums)-1


while(s<=e):
    mid = s + (e-s)//2    

    missing = nums[mid] - (mid+1)

    if missing<k:
        s= mid+1


    else:
        e = mid-1

ans = k + e + 1
print(ans)