def can_split_array(nums, n):
    def count_subarrays(m):
        count = 0
        curr_sum = 0

        for num in nums:
            curr_sum += num
            if curr_sum >= m:
                count += 1
                curr_sum = 0

        return count

    left, right = max(nums), sum(nums)

    while left < right:
        mid = left + (right - left) // 2
        num_subarrays = count_subarrays(mid)

        if num_subarrays >= n:
            left = mid + 1
        else:
            right = mid

    return count_subarrays(left) >= n

# Example usage:
nums = [1, 1]
n = 3
print(can_split_array(nums, n))  # Output: True
