nums = [8 ,17 ,13 ,19 ,10 ,3 ,20 ,5]
n = len(nums)
dp = [1]*n
nums.sort()
hash = [0]*n
x  =0
for i in range(n):
    hash[i] = i
    for j in range(0, i):
        if nums[i]%nums[j]==0 and 1+dp[j] > dp[i] :
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