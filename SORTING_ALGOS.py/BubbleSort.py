arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    swapped = False
    for j in range( n-i-1):
        if arr[j] >arr[j+1]:
            swapped =True
            arr[j] , arr[j+1] = arr[j+1] ,arr[j]

    if swapped == False:
        break

print(arr)