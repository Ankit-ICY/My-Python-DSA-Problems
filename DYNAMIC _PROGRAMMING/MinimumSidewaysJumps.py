class Solution:
    def minSideJumps(self, nums) -> int:
        n = len(nums)-1
        def solve(nums,frog,ind,dp):
            if ind==n:
                return 0

            if (frog, ind) in dp:
                return dp[(frog,ind)]

            if nums[ind+1]!= frog:
                dp[(frog,ind)] =  solve(nums,frog,ind+1,dp)
                return dp[(frog,ind)]
            else:
                ans = 1e9
                for i in range(1,4):
                    if frog != i and nums[ind] != i:
                        ans = min ( ans , 1 + solve(nums,i,ind+1,dp))
                dp[(frog,ind)] = ans
                return ans

            

        frog = 2
        ind = 0
        dp ={}
        return solve(nums,frog,ind,dp)