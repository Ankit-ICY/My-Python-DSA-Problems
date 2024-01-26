def ExpressionOp(s, target,ind,ans,string,total):
    if ind==len(s) :
        total = string[0:len(string)-1]
        if eval(total) == target:
            ans.append(total)
        return string
    

    # ADD OPERATOR
    string+=s[ind] + '+'
    ExpressionOp(s, target,ind+1,ans,string,total)
    string[:-1]
    string[:-1]


    string+=s[ind] + '*'
    ExpressionOp(s, target,ind+1,ans,string,total)
    string[:-1]
    string[:-1]


    string+=s[ind] + '-'
    ExpressionOp(s, target,ind,ans,string,total)
    string[:-1]
    string[:-1]


    return ans




num = "123"
total = ""
target = 6
ind =0 
ExpressionOp(num, target,ind,[],"" ,total) 