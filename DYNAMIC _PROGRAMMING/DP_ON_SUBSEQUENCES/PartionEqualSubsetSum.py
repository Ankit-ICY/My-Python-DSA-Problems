
class Solution:
    def equalPartition(self, n, nums):
        target  = sum(nums)//2
        dp = {}
        ind = 0
        return  self.solve(nums,n,target,dp,ind)
        
        
    def solve(self,nums,n,target,dp,ind):
        if target == 0:
            return "YES"
    
        if ind>=n:
            return "NO"
        
        if (ind,target) in dp:
            return dp[(ind,target)] 
        
        if nums[ind]<=target:
            x1 = self.solve(nums,n,target-nums[ind],dp,ind+1)
            x2 = self.solve(nums,n,target,dp,ind+1)
            dp[(ind,target)] = x1 or x2
            return dp[(ind,target)] 
    
        else:
            dp[(ind,target)]  = self.solve(nums,n,target,dp,ind+1)
            return dp[(ind,target)] 
            
        return "NO"

ob = Solution()
n = 4
nums  = [1,5,11,5]
print(ob.equalPartition(n , nums))
