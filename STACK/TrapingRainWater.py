nums = [0,1,0,2,1,0,1,3,2,1,2,1]

l = 0
r= len(nums)-1
leftmax = nums[l]
rightmax = nums[r]

ans = 0
while l<r:
    if leftmax<rightmax:
        l+=1
        leftmax = max(leftmax, nums[l])
        ans +=leftmax- nums[l]

    else:
        r-=1
        rightmax = max(rightmax, nums[r])
        ans +=rightmax- nums[r]

print(ans)






# stack = [nums[0]]
# ans = 0
# for i in range(1,len(nums)):
#     while(stack and stack[0]<nums[i] ):
#         if len(stack)==1:
#             stack.pop()

#         else:
#             mini = min(stack[0] , nums[i])
#             ans += (mini -stack[-1])
#             stack.pop()


#     stack.append(nums[i])


# print(stack)
# print(ans)

