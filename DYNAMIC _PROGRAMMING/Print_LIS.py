nums =  [1]
n = 1
hash = []
dp = [1]*n
hash = [0]*n
x  =0
for i in range(n):
    hash[i] = i
    for j in range(0, i):
        if nums[i]>nums[j] and 1+dp[j] > dp[i] :
            dp[i] = 1+dp[j]
            hash[i]=j
        

maxi = max(dp)
x = dp.index(maxi)

ans= []
ans.append(nums[x])
while(hash[x]!=x):
    x = hash[x]
    ans.append(nums[x])

ans.reverse()

print(ans)