nums =[[1,10],[3,3]]
people = [3,3,2]

from heapq import heapify, heappop, heappush
people = [(p,i) for i,p in enumerate(people)]
start  = [ nums[f][0] for f in range(len(nums))  ]
end  = [ nums[f][1] for f in range(len(nums))  ]

heapify(start)
heapify(end)

count =0 

ans = [0] *len(people)

for p,i in sorted(people):

    while start and start[0]<=p:
        count+=1
        heappop(start)


    while end and end[0] < p:
        count-=1
        heappop(end)

    ans[i] = count  
   

print(ans)