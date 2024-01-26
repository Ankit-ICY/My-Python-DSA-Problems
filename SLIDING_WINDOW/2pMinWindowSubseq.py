s1 =  "geeksforgeeks"
s2 = "eksrg"
ans = ""
k = 0
maxi = 0
count = 0
j = 0
while  j < len(s1):
    if s1[j] == s2[k]:

        k+=1

    
    if k == len(s2):
        i = j
        k-=1
        while k>=0 and i >= 0:
            if s2[k] ==  s1[i]:
                k-=1
            
            i-=1
        
        i+=1
        if j - i >maxi:
            ans = s1[i : j+1]
            maxi = j-i

        j = i
        k+=1
        
    
    j+=1

print(ans)

