x = 45

s = 1
e = x
mid = s + (e-s)//2
ans = 0 

while(s<=e):
    if mid*mid <= x:
        ans = mid
        s = mid+1

    elif mid*mid>x:
        e = mid-1


    mid = s + (e-s)//2


print(ans)