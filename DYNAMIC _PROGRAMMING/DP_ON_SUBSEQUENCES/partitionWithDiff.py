# class Solution:
#     def countPartitions(self, n, d, nums):
#         total = sum(nums)
        
#         if (total-d)%2==1 or (total-d)<0:
#             return 0
#         target = (total-d)//2
#         ind = 0
#         dp = {}
#         mod = 1e9 + 7
#         return int(self.solve(nums,ind,target,n-1,dp,mod)%mod)


#     def solve(self,nums,ind,target,n,dp,mod):
    
#         if n==0  :
#             if target==0 and nums[0] == 0:
#                     return 2
                    
#             if target==0 or nums[0]==target:
#                 return 1
                    
#             return 0
    
        
#         if (n,target) in dp:
#             return dp[(n,target)]
    
#         if nums[n]<=target:
#             x1 = self.solve(nums,ind,target-nums[n],n-1,dp,mod)
#             x2 = self.solve(nums,ind,target,n-1,dp,mod)
#             dp[(n,target)] = (x1 + x2) % mod
#         else:
#             dp[(n,target)] = self.solve(nums,ind,target,n-1,dp,mod)
            
#         return dp[(n,target)]
    



nums = [1, 1, 1, 1]
d= 0
total = sum(nums)
target = (total-d)//2
n = 4
dp = []
total = sum(nums)
for i in range(n):
    a = []
    for j in range(total+1):
        a.append(False)
    dp.append(a)


if nums[0] == 0:
    dp[0][0] = 2

else:
    dp[0][0] = 1


if nums[0] != 0 and nums[0]<=target :
    dp[0][nums[0]] =1


for i in range(1,n):
    for j in range(0 , target+1):
        notTake = dp[i-1][j]
        take = 0
        if nums[i]<=j :
            take = dp[i-1][j-nums[i]]

        dp[i][j] = take + notTake


# print(dp)
print(dp[n-1][j])