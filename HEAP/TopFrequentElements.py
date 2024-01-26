nums =[1]
k = 1

dic = {}
for i in range(len(nums)):
    if nums[i] not in dic:
        dic[nums[i]] = 1

    else:
        dic[nums[i]] +=1 


from heapq import heappop, heapify ,heappush
heap = []
for i ,j in dic.items():
    heappush(heap , [-j, i] )

ans =[]

for i in range(k):
    x = heappop(heap)
    ans.append(x[1])



print(ans)