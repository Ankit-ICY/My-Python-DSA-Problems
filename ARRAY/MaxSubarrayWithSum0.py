class Solution:
    def maxLen(self, n, nums):
        #Code here
        
        map = {0:-1}
        ans = 0
        sum = 0
        for  i in range(n):
            sum+=nums[i]
            
            
            if sum in map:
                ans = max(ans, i- map[sum])
            else:
                map[sum] = i
                
                
        return ans
                