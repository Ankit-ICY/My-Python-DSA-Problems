def wordBreak(wordDict , s , ind):
    if ind==len(s):
        return True
    
    for i in range(ind,len(s)):
        if s[ind:i+1] in wordDict and  wordBreak(wordDict , s , i+1):
            return True
        else:
            continue


    return False


s = "applepenapple"
wordDict =["apple","pen"]

print(wordBreak(wordDict , s , 0))