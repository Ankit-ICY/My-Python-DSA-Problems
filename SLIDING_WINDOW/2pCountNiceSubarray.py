
nums = [1,1,2,1,1]
k = 4
final = []
for x in range(2):
    count = 0
    i = 0
    j = 0
    temp = 0
    ans = 0
    k-=1
    while(j<len(nums)):
        if nums[j]%2!=0:
            temp+=1
        

        if temp>k:
            while(temp>k):
                if nums[i]%2==1:
                    temp-=1
                count+=1
                i+=1

        
        ans +=count
        j+=1

    final.append(ans)

print(abs(final[0] -final[1]))

# nums = [2,2,2,1,2,2,1,2,2,2]
# k = 2
# count = 0
# i = 0
# j = 0
# temp = 0
# ans = 0
# while(j<len(nums)):

#     if nums[j]%2!=0:
#         temp+=1
#         count = 0

#     if temp==k:
#         while(nums[i]%2==0):
#             count+=1
#             i+=1
#         count+=1
#         i+=1
#         temp-=1
    
#     ans +=count
#     j+=1

# print(ans)