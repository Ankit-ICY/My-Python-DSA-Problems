import bisect

def find_lower_bound(arr, target):
    index = bisect.bisect_left(arr, target)
    return arr[index] if index < len(arr) else 10000000000


nums =[1000000000]

k = 0

ans  = 1e9
for i in range(len(nums)-k):
    ans = min(ans ,abs(nums[i] - find_lower_bound(nums, nums[i])))

# nums.reverse()

# for i in range(len(nums)-k):
#     ans = min(ans ,abs(nums[i] - find_lower_bound(nums[i+k:], nums[i])))


print(ans)


import bisect

def lower_bound(arr, target):
    index = bisect.bisect_left(arr, target)
    return arr[index] if index < len(arr) else None

def upper_bound(arr, target):
    index = bisect.bisect_right(arr, target)
    return arr[index] if index < len(arr) else None

# Example usage:
nums = [2, 3, 3, 5, 10, 15]
target = 3

lower_bound_value = lower_bound(nums, target)
print("Lower bound of", target, "in the array:", lower_bound_value)

upper_bound_value = upper_bound(nums, target)
print("Upper bound of", target, "in the array:", upper_bound_value)

