class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:return 0
        string = ""
        sign = 0
        i = 0
        while(i<len(s) and s[i]==' ' ):
            i+=1

        if len(s) == i:return 0

        s = s[i:]
        if s[0] == '-':
            sign = -1

        else:
            sign  = 1
        
        if s[0] =='+' or s[0] == '-':
            i = 1

        else:
            i = 0


        while(i<len(s)):
            if not s[i].isdigit() or s[i]==' ' or s[i]=='.':
                break

            string+=s[i]
            i+=1

        if string or string.isdigit()==True:
            ans = sign * int(string)
        else:
            return 0


        if (-2**31<=ans<=(2**31)-1): return ans
        elif ans<0: return -2**31
        else : return 2**31-1

        