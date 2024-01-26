arr = [10, 22, 12, 3, 0, 6]
leader = []
leader.append(arr[-1])

i = len(arr)-2
while(i>=0):
    maxi = max(arr[i+1:])
    if arr[i]>maxi:
        leader.append(arr[i])
    i-=1

leader.reverse()
print(leader)
