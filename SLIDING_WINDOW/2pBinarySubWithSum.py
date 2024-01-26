class Solution:
    def numSubarraysWithSum(self, nums, goal: int) -> int:
        
        return self.slide(nums,goal) - self.slide(nums,goal-1)


    def slide(self,nums,goal):
        if goal<0:
            return 0
        i = 0
        ans = 0
        sum = 0
        for j in range(len(nums)):
            sum+=nums[j]

            while(i<=j and sum>goal):
                if nums[i]==1:
                    sum-=1
                
                i+=1

            ans +=j-i+1


        return ans
                    
