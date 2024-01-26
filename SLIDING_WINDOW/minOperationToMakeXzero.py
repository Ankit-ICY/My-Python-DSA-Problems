# nums = [1,1,4,2,3]
# x = 5
# target = sum(nums) - x

# # if target == 0:
# #     print(len(nums)) 

# # if target < 0:
# #     print(-1)

# left, curr_sum, max_length = 0, 0, -1

# for right, num in enumerate(nums):
#     curr_sum += num

#     while curr_sum > target:
#         curr_sum -= nums[left]
#         left += 1

#     if curr_sum == target:
#         max_length = max(max_length, right - left + 1)


# print(max_length)
# if max_length == -1:
#     print(-1)

# else:
#     print(len(nums) - max_length) 

def solve(nums,k,i,j,dp):
    if i>j:
        return 0

    ans = 1e9
    if k ==0:
        return 0

    if nums[j]<=k:
        ans = min(ans , 1+solve(nums,k-nums[j],i,j-1,dp))

    if nums[i]<=k:
        ans = min(ans,1 + solve(nums,k-nums[i],i+1,j,dp))

    
    return ans


    



nums = [1,1]
k = 3
i = 0
j = len(nums)-1

dp ={}
print(solve(nums,k,i,j,dp))