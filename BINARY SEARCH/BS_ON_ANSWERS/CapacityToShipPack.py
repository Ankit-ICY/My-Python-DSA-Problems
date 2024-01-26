def boolCheck(mid , nums , days):
    total = 0
    d = 1
    for i in range(len(nums)):
        if total+nums[i]<=mid:
            total +=nums[i]

        else:
            total = nums[i]
            d +=1

    if d<=days:return True
    return False

nums = [1,2,3,1,1]
days = 4
sum = 0
maxi = 0
for   i in nums:
    if i >maxi:
        maxi = i
    sum+=i

s = maxi
e = sum
ans = 0
mid = s + (e-s)//2

while(s<=e):
    if boolCheck(mid , nums , days):
        ans = mid
        e = mid-1

    else:
        s = mid+1

    mid = s + (e-s)//2

    
print(s)