nums = [4,3,2,7,8,2,3,1]

from collections import Counter
nums = Counter(nums)
ans = []
for i , j in nums.items():
    if j>1:
        ans.append(i)

print(ans)