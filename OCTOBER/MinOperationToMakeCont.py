# class Solution(object):
#     def minOperations(self, A):
#         n = len(A)
#         ans = n
#         hash_set = set()
    
#         for x in A:
#             hash_set.add(x)
    
#         unique = list(hash_set)
#         unique.sort()
    
#         j = 0
#         m = len(unique)
    
#         for i in range(m):
#             while j < m and unique[j] < unique[i] + n:
#                 j += 1
#             ans = min(ans, n - j + i)
    
#         return ans
        
        
# nums = [1,10,100,1000]
# ob = Solution()
# ans = ob.minOperations(nums)
# print(ans)


nums = [1,10,100,1000]

nums = list(set(nums))
nums.sort()
i = 0 
j = len(nums)-1

while i<=j:
    mini = nums[i]
    if nums[i] != nums[i] +1:
        nums[j] = nums[i]+1
        j-=1