nums =[7 ,10, 4 ,3 ,20 ,15]
k = 3
s = []
for i in range(len(nums)):
    if s and len(s)>k:
        s.pop()
        

    if s and nums[i]<s[-1]:
        x = len(s)-1
        while(x>=0 and nums[i]<s[x]):
            x-=1

        s.insert(x+1, nums[i])
        continue

    s.append(nums[i])

if len(s)>k:
    s.pop()
    


print(s[-1])