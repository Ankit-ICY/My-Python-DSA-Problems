def partition(nums,l,r,p):

    while l<r:
        while l<r and  nums[l]<=nums[r]:
            r-=1

        nums[r],nums[l] = nums[l] , nums[r]

        while l<r and  nums[l]<=nums[r]:
            l+=1
            
        nums[r],nums[l] = nums[l] , nums[r]
        

    return l


def QuickSort(nums,n,l,r,p):
    if l>=r:
        return 
    
    pos = partition(nums,l,r,p)
    QuickSort(nums,n,l,pos-1,p)
    QuickSort(nums,n,pos+1,r,p)




nums = [4, 1, 3, 9, 7]
n = len(nums)
l = 0
p = 0
r = n-1
QuickSort(nums,n,l,r,p)


print(nums)




# def partition(nums,l,r,p):

#     while(l<r):
        
#         while(l<r and nums[r]>= nums[l]):
#             r-=1
#         nums[r],nums[l] = nums[l] , nums[r]


#         while(l<r and nums[l]<=nums[r]):
#             l+=1

#         nums[r],nums[l] = nums[l] , nums[r]


#     return l        



# def QuickSort(nums,n,l,r,p):
#     if l>=r:
#         return 
    
#     pos = partition(nums,l,r,p)
#     QuickSort(nums,n,l,pos-1,p)
#     QuickSort(nums,n,pos+1,r,p)




# nums = [4, 1, 3, 9, 7]
# n = len(nums)
# l = 0
# p = 0
# r = n-1
# QuickSort(nums,n,l,r,p)


# print(nums)


