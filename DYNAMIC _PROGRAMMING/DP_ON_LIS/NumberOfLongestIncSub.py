nums = [1,3,5,4,7]
dp = [1]*len(nums)
cn = [1]*len(nums)

for i in range(len(nums)):
    for j in range(0, i):
        if nums[j]<nums[i] and 1+dp[j] > dp[i] :
            dp[i] = 1+dp[j]
            cn[i] = cn[j]
        elif nums[j]<nums[i] and 1+dp[j] == dp[i]:
            cn[i]+= cn[j]
            
no = 0
maxi = max(dp)
for i in range(len(nums)):
    if dp[i]==maxi:
        no+=cn[i]


print(dp)
print(cn)