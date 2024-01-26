nums = [1,2,3,4,5,6,1]
k = 3
n = len(nums)
count = n-k

total = sum(nums)
score= 0
ans = 0
i = 0
j = 0
while(j<n):
    if count == 0:
        if ans<total-score:
            ans = total - score
        count+=1
        score -=nums[i]
        i+=1

    else:
        score +=nums[j]
        count-=1
        j+=1

print(ans)
    