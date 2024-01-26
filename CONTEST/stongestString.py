MOD = 10**9 + 7

def countSteppingNumbers(low, high):
    low_num = int(low)
    high_num = int(high)
    result = []

    def dfs(num):
        if num > high_num:
            return
        if low_num <= num <= high_num:
            result.append(num)
        
        last_digit = num % 10

        if last_digit > 0:
            dfs(num * 10 + last_digit - 1)
        
        if last_digit < 9:
            dfs(num * 10 + last_digit + 1)

    for i in range(1, 10):  # Start with single-digit numbers
        dfs(i)

    return len(result) % MOD

# Test case
low = "90"
high = "101"
output = countSteppingNumbers(low, high)
print(output)  # Output: 10
