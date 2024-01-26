nums =[1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1]

k = 2
zero = 0
count = 0 
i = 0
ans = 0
for j in range(len(nums)):
    

    if nums[j] == 1:
        count+=1

    elif nums[j] == 0:
        zero +=1
        count+=1

    
    if zero>k:
        while(nums[i]!=0):
            count-=1
            i+=1

        count-=1
        zero-=1
        i+=1
    ans = max(count,ans)

ans = max(ans,count)
print(ans)
