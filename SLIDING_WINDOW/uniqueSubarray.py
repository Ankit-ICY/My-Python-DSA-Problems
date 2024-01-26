nums =[1,2,2]

m = 2
k = 2
dic ={}
count = 0
j  =0 
ans  = 0
sum = 0
for i in range(len(nums)):

    if nums[i] in dic:
        dic[nums[i]] +=1
        count +=1
        sum += nums[i]

    else:
        dic[nums[i]] = 1
        count+=1
        sum += nums[i]

    
    if count==k:
        while count ==k:
            if len(dic)>=m:
                ans= max(ans,sum)

            dic[nums[j]]-=1
            if dic[nums[j]] == 0:
                del dic[nums[j]]
            count-=1
            sum-=nums[j]
            j+=1

print(ans)