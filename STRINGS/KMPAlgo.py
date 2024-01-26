

s = "ab"
i = 0
j = 1
n = len(s)
pre = [0] *n

while(j<n):
    if s[i] == s[j]:
        pre[j] = i+1
        i+=1
        j+=1

    else:   
        if i==0:
            j+=1

        else:
            i  = pre[i-1]


print(pre)

