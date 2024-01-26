nums = [1,1,1]


k = 2
n = len(nums)
pre = {}
sum = 0
count = 0
for i in range(n):
    sum+=nums[i]
    if sum-k==0:
        count+=1
    if sum-k in pre :
        count+=pre[sum-k]
    
    if sum in pre:
        pre[sum]+=1
    else:
        pre[sum] = 1


print(count)