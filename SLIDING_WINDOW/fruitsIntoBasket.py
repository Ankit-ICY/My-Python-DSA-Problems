nums = [3,3,3,1,2,1,1,2,3,3,4]
i = 0
count =0
dic = {}
ans = 0
for j in range(len(nums)):

    if  nums[j] not in dic:
        dic[nums[j]] = 1
        count+=1

    else:
        dic[nums[j]]+=1

    if count>2:
        while(count>2):
            dic[nums[i]]-=1
            if dic[nums[i]] == 0:
                count-=1
                del dic[nums[i]]

            i+=1

    ans = max(ans , sum(dic.values()) )

print(ans)
