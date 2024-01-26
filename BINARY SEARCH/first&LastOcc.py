nums = [5,7,7,8,8,10]
target = 8
n = len(nums)
ans =0 
sol = [-1,-1]
for i in range(2):
    ans = -1
    s = 0
    e = n-1
    mid = s + (e-s)//2
    while(s<=e):
        if nums[mid]==target:
            ans = mid
            if i==0:e = mid-1
            else:
                s= mid+1

        elif nums[mid]>target:
            e = mid-1

        else:
            s = mid+1

        mid = s + (e-s)//2
    
    sol[i] = ans


print(sol)