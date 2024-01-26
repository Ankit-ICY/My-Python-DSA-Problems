nums = [1,1,1]
k = 2
map = {}
sum =0
count =0
map[0] = 1
for i in range(len(nums)):
    sum +=nums[i]
    remove = sum-k
    if remove in map.keys():
        count+=map[remove]
    if sum in map:
        map[sum]+=1 
    else:
        map[sum]= 1
   

print(count)






# def SubArrSum(nums,ind,k,dp):
#     if ind>=len(nums):
#         return 0
    
#     if k<=0:
#         return 1

#     sum =0

#     x= 0
#     for i in range(ind,len(nums)):
#         sum+=nums[i]
#         if sum==k:
#             x+=1
    
#     x = x + SubArrSum(nums,ind+1,k,dp)
 
#     return x


# nums = [1,1,1]
# k = 2
# ind =0
# dp ={}
# print(SubArrSum(nums,ind,k,dp))