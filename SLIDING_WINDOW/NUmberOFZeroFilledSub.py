nums = [0,0,0,2,0,0]
ans = 0
count = 0
temp = 1
for i in range(len(nums)):
    if nums[i]==0 and count==0:
        count = 1
        temp +=1

    elif count >0 and nums[i]==0:
        
        count =count + temp
        temp+=1

    else:
        ans +=count
        temp =1
        count = 0

ans +=count


print(ans)