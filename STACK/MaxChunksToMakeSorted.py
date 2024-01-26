arr = [2,1,3,4,4]
n = len(arr)


maxi = arr[0]
count = 1
for i in range(1,n):
    if arr[i] >= maxi :
        if i>=maxi:
            count+=1
        maxi = arr[i]

print(count)
       

