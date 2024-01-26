def binaryStrings(k,ans, string,one):
    if len(string)==k:
        ans.append(string)
        return
    
    
    binaryStrings(k,ans, string+'0',1)
    if one==1:
        binaryStrings(k,ans, string+'1',0)


    return ans


k = 3 
one = 1
print(binaryStrings(k,[], '',one))
