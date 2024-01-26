
def rev(num):
    num = str(num)
    num = num[::-1]
    num = int(num)
    return num

def countPairs(nums,i,j,dp):
    x = 0
    if i>=j:
        return 0

    if nums[i] + rev(nums[j]) == nums[j] + rev(nums[i]):
        x1 = 1 + countPairs(nums,i+1,j,dp) 
        x2 =    1 + countPairs(nums,i,j-1,dp) 
        x = x1 or x2

    else:
        x1 = countPairs(nums,i+1,j,dp)
        x2 = countPairs(nums,i,j-1,dp)
        x = x1 + x2

    return x

nums = nums = [42,11,1,97]

i = 0
j = len(nums)-1

print(countPairs(nums,i,j,{}))

# def reverse(num):
#     num = str(num)
#     num = num[::-1]
#     num = int(num)
#     return num

# nums = nums = [13,10,35,24,76]

# for i in range(len(nums)):
#     nums[i] = (nums[i] - reverse(nums[i]))

# print(nums)
# from collections import Counter

# nums = Counter(nums)
# print(nums)
# count = 0
# for i ,j in nums.items():
#     if j>1:
#         count+= j*(j-1)//2
    
# print(count)