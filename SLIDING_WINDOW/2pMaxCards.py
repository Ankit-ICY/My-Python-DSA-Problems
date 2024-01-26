nums = [1,2,3,4,5,6,1]
k = 3

i = 0
j =0

prefix = [0]*len(nums)
prefix[0] = nums[0]
for i in range(1,len(nums)):
    prefix[i] = prefix[i-1] + nums[i]


ans =0
sum=0
i = 0
while(j<len(nums)):
    sum=prefix[j]

    if j-i==k:
        sum-=prefix[i]
        i+=1
        ans = max(ans,sum)
        

    j+=1

print(ans)