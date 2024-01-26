def keyPad(options,string, n,ans,ind):
    if ind==len(n):
        ans.append(string)
        return
    
    m = int(n[ind])
    str = options[m]
    for i in range(len(str)):
        keyPad(options,string+str[i], n,ans,ind+1)
    
    return ans

n = "23"

options = ["" , "" , "abc" , "def" , "ghi" , "jkl", "mno" , "pqrs", "tuv" , "wxyz"]
string = ""
ans =[]
ind = 0
print(keyPad(options,string, n ,ans,ind))



# def keyPad(options,string, n,ans):
#     if n==0:
#         ans.append(string)
#         return
#     m = n%10
#     str= options[m]
#     for i in range(len(str)):
#         keyPad(options, str[i]+string, n//10,ans)
    
#     return ans

# n = 233

# options = ["" , "" , "abc" , "def" , "ghi" , "jkl", "mno" , "pqrs", "tuv" , "wxyz"]
# string = ""
# ans =[]
# print(keyPad(options,string, n ,ans))