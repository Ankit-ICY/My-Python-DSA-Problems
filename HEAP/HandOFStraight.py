hand = [1,1,2,2,3,3]

groupSize = 3
hand.sort()
dic=  {}
for i in range(len(hand)):
    if hand[i] in dic:
        dic[hand[i]] +=1
    else:
        dic[hand[i]] = 1


minH = list(dic.keys())

import heapq 
heapq.heapify(minH)
count = 0
while minH:
    first = minH[0]
    count = 0
    for i in range(first, first + groupSize):
        if i in dic and dic[i] >0:
            count+=1
            dic[i]-=1
            if dic[i]==0:
                heapq.heappop(minH)

        else:
            print(False)
            break
    
    if count == groupSize:
        continue
    else:
        break