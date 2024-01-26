def generateParenthesis(n , ans, total , string , open, close):
    if len(string) == total and string not in ans: 
        ans.append(string)
        return string
    

    if open< n :
        string+='('
        generateParenthesis(n , ans, total , string , open+1, close)
        string = string[:-1]

    if close < n and open>close:
        string+=')'
        generateParenthesis(n , ans, total , string , open, close+1)
        string = string[:-1]


    return ans

n = 3
total = 2*n
ans =[]
string = ""
open = 0
close = 0
print(generateParenthesis(n , ans, total , string , open, close))