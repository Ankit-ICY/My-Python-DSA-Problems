
# BRUTE FORCE
# nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
# n = len(nums)
# pos =[]
# neg = []
# for i in range(n):
#     if nums[i]<0:
#         neg.append(nums[i])
#     else:
#         pos.append(nums[i])

# ans = []

# for i in range(n//2):
#     ans.append(pos[i])
#     ans.append(neg[i])

# print(ans)
    




# nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
# n = len(nums)
# ans = [0]*n
# neg = 1
# pos = 0
# for i in range(n):
#     if nums[i]<0:
#         ans[neg] = nums[i]
#         neg+=2
#     else:
#         ans[pos] = nums[i]
#         pos+=2

# print(ans)



# if nums[0]<0:
#     temp = nums[0]
#     nums[0] = nums[1]
#     nums[1] = temp

# sign = 0
# i  =1
# while(i<len(nums)-1):
#     if sign ==0:
#         if nums[i]<0:
#             i+=1
#             sign =1
#             continue
#         else:
#             temp = nums[i]
#             nums[i] = nums[i+1]
#             nums[i+1] = temp
#             i+=2
        
#     elif sign ==1:
#         if nums[i]>0:
#             i+=1
#             sign =0
#             continue
#         else:
#             temp = nums[i]
#             nums[i] = nums[i+1]
#             nums[i+1] = temp
#             i+=2

# print(nums)
        
    
