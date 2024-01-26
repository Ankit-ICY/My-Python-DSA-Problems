nums1 = [-10,-4,0,0,6]
nums2 =[3,5,6,7,8,100]
k = 10
pq = []
for i in range(len(nums1)):
    for j in range(len(nums2)):
        sum = nums1[i]+ nums2[j]

        if len(pq)<k:
            pq.append([sum,nums1[i],nums2[j]])

        elif sum<pq[0][0]:
            pq.pop()
            pq.append([sum,nums1[i],nums2[j]])

        else:
            break
            # x= 0
            # while x<len(pq) and  sum>pq[x][0]:
            #     x+=1
            # if x == len(pq):
            #     break
            # else:
            #     pq.pop(x+1)
            #     pq.insert(x, [sum,nums1[i],nums2[j]])
            


for i in range(len(pq)):
    pq[i] = pq[i][1:]

print(pq)