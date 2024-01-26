class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: 
        if len(s1) > len(s2): 
            return False
        from collections import Counter
        dic = Counter(s1)
        count = len(dic)

        i = 0

        for j in range(len(s2)):
            if s2[j] in dic:
                dic[s2[j]] -= 1
                if dic[s2[j]] == 0:
                    count -= 1
            
            if count == 0:    
                while count == 0:
                    if count == 0 and j-i + 1==len(s1):
                        return True
                    elif s2[i] in dic:
                        dic[s2[i]] +=1
                        if dic[s2[i]] >0:
                            count+=1
                    
                    i+=1

        return False
                            

s1 = "ab"
s2 = "eidboaoo"
solution = Solution()
print(solution.checkInclusion(s1, s2))  