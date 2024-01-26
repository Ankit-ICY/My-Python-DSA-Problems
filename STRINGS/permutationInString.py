s1 = "trinitrophenylmethylnitramine"
s2 = "dinitrophenylhydrazinetrinitrophenylmethylnitramine"


from collections import Counter
dic = Counter(s1)
count = len(dic)

j = 0
i = 0

for j in range(len(s2)):

    if j-i == len(s1) :
        
        if s2[i] in dic:
            dic[s2[i]]+=1
            if dic[s2[i]]>0:
                count+=1

        i+=1


    if s2[j] in dic:
        dic[s2[j]]-=1
        if dic[s2[j]] == 0:
            count-=1
    

    if count == 0:
        print(True)
        break

    
    


# while(j<len(s2)):
#     if s2[j] in dic:
#         dic[s2[j]] -=1
#         if dic[s2[j]] ==0:
#             count-=1
#         j+=1
        
#     else:
#         j+=1

#     if count == 0:
#         print(True)
#         break

#     if j-i == len(s1):

#         if s2[i]in dic:
#             dic[s2[i]] +=1
#             if dic[s2[i]]>0:
#                 count+=1

#         i+=1
        
   