s1 = "mississippi"
s2 = "issipi"

j=0
i = 0

while(i<len(s1)):
    if s1[i] == s2[j]:
        j+=1
        i+=1


    else:
        if j>0:

            while(j>=0 and s1[i] != s2[j] ):
                j-=1
            j+=1
        i+=1



    if j ==len(s2):
        
        print(len(s2) - i )
        break



