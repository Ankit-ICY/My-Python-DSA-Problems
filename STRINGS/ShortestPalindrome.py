# s = "abcd"
# maxi = 0
# n = len(s)
# for i in range(n):
#     if s[0:i] == s[0:i][::-1]:
#         maxi = max(maxi,i)


# s = s[maxi:][::-1] + s
# print(s)

s = "pppp"

str =  s[::-1] + '$' + s
# print(str)
i = 0 
j = 1
n  = len(str)
pre = [0]*n
while(j<n):
    if str[i] == str[j]:    

        pre[j] = i+1 
        
        i+=1
        j+=1

    else:
        if i == 0:
            j+=1

        else:
            i = pre[i-1]


maxi= pre[-1]

print(pre)
s = s[maxi:][::-1] + s
print(s)