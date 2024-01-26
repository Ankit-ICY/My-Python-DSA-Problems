
class Solution:
    def subarraysWithKDistinct(self, nums, k) :
        return abs(self.slide(nums,k)-self.slide(nums,k-1))


    def slide(self,nums,k):
        dic={}
        c = 0
        i = 0
        ans = 0
        for j in range(len(nums)):
            if nums[j] not in dic:
                dic[nums[j]] = 1

            elif nums[j] in dic:
                dic[nums[j]]+=1

            if len(dic)>k:

                while(len(dic)>k):
                    c+=1
                    if nums[i] in dic:
                        dic[nums[i]]-=1
                        if dic[nums[i]]==0:
                            del dic[nums[i]]

                    i+=1

            ans+=c


        return ans


