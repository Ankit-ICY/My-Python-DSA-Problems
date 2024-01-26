def power(str,ind,ans,n,string):
    if string : 
        ans.append(string)

    for i in range(ind, n):
        string+=str[i]
        power(str,i+1,ans,n,string)
        string = string[:-1]


    return ans
        

str = "ggg"
ind = 0
n = len(str)
string = ""
ans = []
print(power(str,ind,ans,n,string))