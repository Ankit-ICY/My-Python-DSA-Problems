hours = [5,1,4,2,2]
target = 6
n = len(hours)
hours.sort()

s  = 0
e= n-1

while s<=e:
    mid = s + (e-s)//2

    if hours[mid] == target:
        e = mid-1
        


    elif hours[mid]>target:
        e = mid-1

    else:
        s = mid+1

print(n-s)
