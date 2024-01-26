class Solution:
    def search(self, nums, target) :
        n = len(nums)
        s = 0
        e = len(nums)-1
        mid = s + (e-s)//2

        while(s<e):
            if nums[mid]>=nums[0]:
                s = mid+1

            else:e = mid

            mid = s + (e-s)//2


        if target>=nums[s]  and target<=nums[n-1]:
            return self.binarySearch(nums,s,n-1,target)

        else:
            return self.binarySearch(nums,0,s,target)

        

    def binarySearch(self,nums,s,e,target):
        mid = s+ (e-s)//2

        while(s<=e):
            if nums[mid]==target:
                return mid

            elif target>nums[mid]:
                s = mid+1

            else:
                e = mid-1

            mid = s+ (e-s)//2

        return -1
            
                

    
