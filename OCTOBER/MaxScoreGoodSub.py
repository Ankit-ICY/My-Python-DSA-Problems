nums = [1,4,3,7,4,5]
k = 3

i = k
j = k
mini = nums[k]
n = len(nums)
ans = nums[k]


while i>0 or j<n-1:
    left = nums[i-1] if i>0 else 0
    right = nums[j+1] if j <n-1 else 0

    if left>right:
        i-=1
        mini = min(left, mini)

    else:
        j+=1
        mini = min(right, mini)

    ans = max(ans, (j-i+1) * (mini) )

print(ans)