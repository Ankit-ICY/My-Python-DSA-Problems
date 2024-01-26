nums =[2,3,7,9,3]
stack = []

for  i in range(len(nums)-1, -1, -1):
    if stack and stack[-1] >= nums[i]:
        ele = stack.pop()
        ele += nums[i]
        stack.append(ele)
        
    else:
        stack.append(nums[i])


print(stack)
















# i = 0
# ans = 0
# for  i in range(len(nums)-1,0,-1):
#     if nums[i] >= nums[i-1]:
#         ans = nums[i] + nums[i-1]
#         nums[i-1] = nums[i] + nums[i-1]
#         nums[i] = 0


# print(ans)

# def solve(nums,ind,element,dp):
#     ans = 0
#     if ind>=len(nums):
#         ans = max(ans,element)
#         return ans + element
#     if element<=nums[ind]:
#         x1 = solve(nums,ind+1,element+ nums[ind],dp)
#         x2 = solve(nums,ind+1,element,dp)
#         x = max(x1,x2)

#     else:
#         x = solve(nums,ind+1,element,dp)

#     return x
# nums =  [5,3,3]
# ind = 1
# element= nums[0]
# dp = {}
# visited = [False]*len(nums)
# print(solve(nums,ind,element,dp))
