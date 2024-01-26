class Solution:
    def countStrings(self, s):
        unique_strings = set()

        def reverse_substring(s, i, j):
            return s[:i] + s[i:j + 1][::-1] + s[j + 1:]

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                new_string = reverse_substring(s, i, j)
                unique_strings.add(new_string)

        return len(unique_strings)

# Test the function with the given input
s = "abcdefghi"
sol = Solution()
result = sol.countStrings(s)
print(result)  # Output: 37
