arr = [1,2,2,3,3,3]
from collections import Counter

arr = Counter(arr)
print(arr)
for i , j in arr.items():
    if i == j:
        print(i)
        break