class Solution:
    def count(self, nums, n, Sum):
        dp ={}
        
    
        return self.solve(n,dp,sum,nums)


    def solve(self,n,dp,sum,nums):
        
        if sum==0:
            return 1
        
        if n<=0:
            return 0
            
            
        if nums[n-1] <=sum:
            x1 = self.solve(n,dp,sum-nums[n-1],nums)
            x2 = self.solve(n-1,dp,sum,nums)
            x = x1 + x2
            
        else:
            x = self.solve(n-1,dp,sum,nums)
            
        
        return x
    
ob=  Solution()

nums  = [1,2,3]
sum = 4
n = 3
print(ob.count(nums,n,sum))