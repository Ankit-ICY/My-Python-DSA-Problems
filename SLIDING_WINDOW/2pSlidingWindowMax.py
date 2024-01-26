nums = [1,3,-1,-3,5,3,6,7]
k = 3
ans =[]
dq = []
count = 0
i = 0
j = 0
while(j<len(nums)):
    if count == k:
        ans.append(dq[0])
        count-=1
        if nums[i]==dq[0]:
            dq.pop(0)
            i+=1
        else:
            i+=1

    elif len(dq)==0 or dq[-1]>nums[j]:
        dq.append(nums[j])
        count+=1
        j+=1
    else:
        while(len(dq)!=0 and dq[-1]<nums[j]):
            dq.pop()
        dq.append(nums[j])
        count+=1
        j+=1        

ans.append(dq[0])
print(ans)

# maxi = 0
# i = 0
# j = 0
# count = 0
# while(j<len(nums)):
#     if count == k:
#         ans.append(maxi)
#         count -=1
#         if nums[i] != maxi:
#             i+=1
#         else:
#             i+=1
#             maxi = -1e9
#             count = 0
#             j = i


#     elif nums[j]>maxi:
#         maxi = nums[j]
#         count+=1
#         j+=1

#     else:
#         count+=1
#         j+=1

# ans.append(maxi)

# print(ans)