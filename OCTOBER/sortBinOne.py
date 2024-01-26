
arr = [10,100,1000,10000]

from collections import defaultdict
dic = defaultdict(list)
for i in range(len(arr)):
    num = str(bin(arr[i])[2:])
    count = num.count('1')  
    dic[count].append(arr[i])


print(dic)
ans = []
maxi = max(dic)

for i in range(maxi+1):
    if i in dic:
        dic[i].sort()
        for j in dic[i]:
            ans.append(j)

print(ans)
