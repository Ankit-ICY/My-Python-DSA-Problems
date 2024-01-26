class Solution:
    def checkValidString(self, s: str) -> bool:
        bracket= 0
        dp ={}
        return self.ValidParenthesis(s,0,dp,bracket)

    def ValidParenthesis(self,s,ind,dp,bracket):
        if ind==len(s):
            if bracket==0:
                return True
            else:
                return False
        if (ind,bracket) in dp:
            return dp[(ind,bracket)]


        if s[ind]=="(":
            dp[(ind,bracket)] = self.ValidParenthesis(s,ind+1,dp,bracket+1)
            return dp[(ind,bracket)]
        elif s[ind]==")" :
            dp[(ind,bracket)]= bracket!=0 and self.ValidParenthesis(s,ind+1,dp,bracket-1)
            return dp[(ind,bracket)]

        else:
            dp[(ind,bracket)]=    self.ValidParenthesis(s,ind+1,dp,bracket+1) or self.ValidParenthesis(s,ind+1,dp,bracket) or bracket!=0 and self.ValidParenthesis(s,ind+1,dp,bracket-1)
            return dp[(ind,bracket)]


        return dp[(ind,bracket)]