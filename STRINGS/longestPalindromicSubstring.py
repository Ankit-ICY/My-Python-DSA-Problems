class Solution:
    def longestPalindrome(self, s):
        size = 0
        ans = ""
        for i in range(len(s)):
            l = i
            r = i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>size:
                    ans = s[l:r+1]
                    size = r-l+1
                l-=1
                r+=1

            l = i
            r = i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>size:
                    ans = s[l:r+1]
                    size = r-l+1
                l-=1
                r+=1
        return ans
        
ob = Solution()
s = "babad"
print(ob.longestPalindrome(s))