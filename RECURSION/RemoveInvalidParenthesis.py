def ValidStr(s):

    stack = []
    for i in range(len(s)):
        if s[i]=="(":
            stack.append("(")

        elif s[i] == ")":
            if stack and  stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")

        else:
            continue

    if stack:
        return False
    return True


def solve(s,ans,ind,invalid,n,string):
    if invalid <0:
        return 0

    if ind>=len(s):
        if len(string)==n and ValidStr(string) and string not in ans:
            ans.append(string)

        return 


    if  s[ind] == "(":
        solve(s,ans,ind+1,invalid,n,string + s[ind])
        solve(s,ans,ind+1,invalid-1,n,string )

    elif s[ind] == ")":
        solve(s,ans,ind+1,invalid,n,string + s[ind])
        solve(s,ans,ind+1,invalid-1,n,string )

    else:
        solve(s,ans,ind +1,invalid,n,string+s[ind])
    
    return ans

def invalidCheck(s):

    stack = []
    for i in range(len(s)):
        if s[i]=="(":
            stack.append("(")

        elif s[i] == ")":
            if stack and  stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")

        else:
            continue

    if stack:
        return len(stack)
    else:
        return 0



s =  "(a)())()"
ans = []
ind=  0
dp = {}
invalid = invalidCheck(s)
open = 0
n = len(s)- invalid
print(solve(s,ans,ind,invalid,n,""))