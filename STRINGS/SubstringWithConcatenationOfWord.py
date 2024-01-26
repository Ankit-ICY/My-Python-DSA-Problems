s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]





size = len(words[0])
n = len(s)
w = len(words)

dic = {}

from collections import Counter
dic = Counter(words)


ans = []

for i in range(n):
    count = 0
    j = i
    dic = Counter(words)
    while j<n:
        string = s[j : j+size]

        if string in dic and dic[string]>0:
            
            dic[string]-=1
            count+=1
            j+=size
    



        else:
            if count==w:
                ans.append(i)
            break

print(ans)

