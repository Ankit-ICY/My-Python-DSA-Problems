# def solve(n,ans,res,s,ind):
#     if ind==n:
#         return s

#     string = ""
#     count = 1
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]:
#             count+=1
#         else:
#             string += str(count) +  s[i]
#             count = 1


#     string += str(count) +  s[-1]
#     ans.append(string)

#     solve(n,ans,res,string,ind+1)


#     return ans






# n= 1

# ans = []
# res =[]
# i = "1"
# ind = 1
# print(solve(n,ans,res,i,ind))





n = 1

# # 112233
j = 1
s = "1"
while(j<n):
    count = 1
    string = s
    s= ""
    for i in range(1,len(string)):
        if string[i]==string[i-1]:
            count+=1
        else:
            s += str(count)  + string[i-1]
            count = 1
    s += str(count)  + string[-1]
    j+=1
            
        
print(s)