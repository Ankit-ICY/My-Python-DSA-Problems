n= 2
m = 9


s = 1 

e = m

mid = s + (e-s)//2

while(s<=e):
    if mid**n==m:
        print(mid)
        break

    elif mid**n>m:
        e = mid-1
    else:
        s= mid+1


    mid = s + (e-s)//2
    
