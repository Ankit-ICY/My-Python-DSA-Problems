nums = [2,3,5]
k=  5
sum = 0
ans = 0
pre = {}
for  i in range(len(nums)):
    sum+=nums[i]
    score = sum - k
    if score == 0:
        ans = max(ans, i+1)
    if score in pre:
        ans = max(ans, i -  pre[score]  )    

    if sum not in pre:
        pre[sum] = i

print(ans)