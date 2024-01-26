arr = [12, 31, 25, 8, 32, 17]
n = 5
for i in range(n-1):
    for j in range(i+1,n):
        if arr[i]>arr[j] :
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp

print(arr)