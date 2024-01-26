class Solution:
    def findTargetSumWays(self, nums, target) :
        if (target + sum(nums))%2!=0:
            return 0
        else:
            target = (target + sum(nums))//2
        n = len(nums)
        dp = {}

        return self.solve(n,target,nums,dp)

    
    
    def solve(self,n,target,nums,dp):
        if n==0:
            if target==0:
                return 1
            else:
                return 0
        elif (n,target) in dp:
            return dp[n,target]
        else:
            item = nums[n-1]
            if item<=target:
                x1 = self.solve(n-1,target-item,nums,dp)
                x2 = self.solve(n-1,target,nums,dp)
                x = x1 +x2
            else:
                x = self.solve(n-1,target,nums,dp)
            dp[(n,target)] =x
            return x
    #     sum = 0
    #     ans = []
    #     ind = 0
    #     m = [False]*len(nums)
    #     return len(self.targetSum(nums,target,ind,sum,ans,m))


    
    # def targetSum(self,nums,target,ind,sum,ans,m):
    #     if ind == len(nums) and sum == target:
    #         ans.append(sum)
    #         return sum
        
    #     if ind<len(nums) and not m[ind]:
    #         sum = sum +nums[ind]
    #         m[ind] = True
    #         self.targetSum(nums,target,ind+1,sum,ans,m)
    #         m[ind] = False
    #         sum = sum - nums[ind]
    #         sum = sum -nums[ind]
    #         self.targetSum(nums,target,ind+1,sum,ans,m)
            
    #     return ans

