nums = [20 ,7 ,9 ,6 ,9 ,21 ,12 ,3 ,12 ,16, 1, 27]

n = len(nums)
dp1 = [1]*n
for i in range(1,n):
    for j in range(0,i):
        if (nums[j] <nums[i] )   and dp1[i] < 1 + dp1[j] :
            dp1[i] = 1 + dp1[j]




dp2 = [1]*n
for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if (nums[j] <nums[i] )   and dp2[i] < 1 + dp2[j] :
            dp2[i] = 1 + dp2[j]


ans = 1

for i in range(n):
    ans = max(ans , dp1[i] + dp2[i]-1  )
print(dp1)
print(dp2)
print(ans)